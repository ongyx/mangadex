#set -x

ARTIFACT_URL="https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.25/swagger-codegen-cli-3.0.25.jar"
ARTIFACT="codegen.jar"

API_SPEC_URL="https://api.mangadex.org/api.yaml"
API_SPEC_DIR="spec"
API_SPEC_LATEST="$API_SPEC_DIR/latest.yaml"

API_NAME="mangadex_openapi"
API_DOCS="api_docs"
API_VERSION="0.2.1"

BUILD_LOG="build.log"

# Any files/folders in this array will be moved out of the old build and then moved into the new build.
declare -a API_KEEP=("wrapper")

argv=("$@")

check_commands () {
  for cmd in curl java black; do
    if ! hash $cmd 2>/dev/null; then
      echo "command $cmd required, go install it first."
      exit 1
    fi
  done
}

die () {
  echo "build failed: $1"
  exit 1
}

keep () {
  for folder in "${API_KEEP[@]}"; do
    mv $API_NAME/$folder .
  done
}

restore () {
  for folder in "${API_KEEP[@]}"; do
    mv $folder $API_NAME/
  done
}

artifact_download () {
  curl --progress-bar -Lo $ARTIFACT $ARTIFACT_URL  
}

spec_download () {
  curl --progress-bar -Lo $API_SPEC_LATEST $API_SPEC_URL
}

spec_create () {
  mkdir $API_SPEC_DIR
  spec_download
}

spec_update () {
  old_filesize=$(du -b $API_SPEC_LATEST | cut -f 1)
  old_version=$(grep -m 1 -oP 'version: \K(.*)$' $API_SPEC_LATEST)

  new_filesize=$(curl -Is $API_SPEC_URL | grep -m 1 -oP 'content-length: \K(.*)$' | tr -d '\r')

  if [ $new_filesize != $old_filesize ]; then
    echo "changes detected, downloading"

    mv $API_SPEC_LATEST "$API_SPEC_DIR/${old_version}.yaml"
    spec_download
  else
    echo "no changes detected"
  fi
}

check_commands

echo "pinging Mangadex for any spec changes..."

if [ ! -d $API_SPEC_DIR ]; then
  echo "spec not found, downloading"
  spec_create
else
  spec_update
fi

if [ "${argv[0]}" == "nogen" ]; then
  exit 1
fi

if [ ! -e $ARTIFACT ]; then
  echo "codegen not found, downloading"
  artifact_download
fi

TMP=$(mktemp -dq) || die "can't create tempdir"
TMP_CONFIG=$(mktemp -q) || die "can't create tempfile"
trap 'rm -rf "$TMP" "$TMP_CONFIG"' EXIT

# create config
cat << EOF > $TMP_CONFIG
{
  "packageName": "$API_NAME",
  "packageVersion": "$API_VERSION"
}
EOF

echo "generating API (full log in $BUILD_LOG)"

java -jar $ARTIFACT generate -i $API_SPEC_LATEST -o $TMP -l python -c $TMP_CONFIG &>$BUILD_LOG

echo "done"

keep

for folder in $API_DOCS $API_NAME; do
  if [ -d $folder ]; then
    rm -r $folder
  fi
done

mkdir $API_DOCS

# move generated code/docs to their correct locations
mv $TMP/{docs,README.md} $API_DOCS
mv $TMP/$API_NAME .

restore

echo "patching API (this might take a while)"

###########
# PATCHES #
###########
# Some parts of the generated code need to be monkey-patched for it to run in the first place.

# Add version string
cat << EOF >> $API_NAME/__init__.py

__version__ = "$API_VERSION"
EOF

# Serialised arrays no longer work when passed to the API; they need to have an '[]' at the end of the array name.
sed -i 's/(k, value)/(k + "[]", value)/g' $API_NAME/api_client.py

# format all API files
black $API_NAME/**

echo "done"
