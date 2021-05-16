#set -x

ARTIFACT_URL="https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.25/swagger-codegen-cli-3.0.25.jar"
ARTIFACT="codegen.jar"

API_SPEC_URL="https://api.mangadex.org/api.yaml"
API_SPEC_DIR="spec"
API_SPEC_LATEST="$API_SPEC_DIR/latest.yaml"

API_NAME="mangadex"
API_DOCS="api_docs"
API_VERSION="0.0.1"

declare -a API_KEEP=("wrapper")

TMP="tmp"
TMP_CONFIG="tmp.json"

check_commands () {
  for cmd in curl diff java; do
    if ! hash $cmd 2>/dev/null; then
      echo "Command $cmd required, go install it first."
      exit 1
    fi
  done
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
  curl -Lo $ARTIFACT $ARTIFACT_URL  
}

spec_download () {
  curl -Lo $API_SPEC_LATEST $API_SPEC_URL
}

spec_create () {
  mkdir $API_SPEC_DIR
  spec_download
}

spec_update () {
  old_filesize=$(du -b $API_SPEC_LATEST | cut -f 1)
  old_version=$(grep -m 1 -oP 'version: \K(.*)$' $API_SPEC_LATEST)

  new_filesize=$(curl -I $API_SPEC_URL | grep -m 1 -oP 'content-length: \K(.*)$')

  if [ new_filesize != old_filesize ]; then
    echo "update detected, downloading"

    mv $API_SPEC_LATEST "$API_SPEC_DIR/${old_version}.yaml"
    spec_download
  else
    echo "no update detected"
  fi
}

check_commands

if [ ! -d $API_SPEC_DIR ]; then
  echo "creating spec"
  spec_create
else
  echo "updating spec"
  spec_update
fi


if [ ! -e $ARTIFACT ]; then
  echo "codegen not found, downloading"
  artifact_download
fi

# create config
cat << EOF > $TMP_CONFIG
{
  "packageName": "$API_NAME",
  "packageVersion": "$API_VERSION"
}
EOF

java -jar $ARTIFACT generate -i $API_SPEC_LATEST -o $TMP -l python -c $TMP_CONFIG

rm $TMP_CONFIG

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

rm -r $TMP

###########
# PATCHES #
###########
# Some parts of the generated code need to be monkey-patched for it to run in the first place.

# Add version string
cat << EOF >> $API_NAME/__init__.py

__version__ = "$API_VERSION"
EOF

# Add 'Object' as a vaild native type (should be lowercase 'object')
# otherwise an AttributeError is raised
cat << "EOF" >> $API_NAME/api_client.py

ApiClient.NATIVE_TYPES_MAPPING["Object"] = object
EOF
