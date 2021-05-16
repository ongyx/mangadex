ARTIFACT_URL="https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.25/swagger-codegen-cli-3.0.25.jar"
ARTIFACT="codegen.jar"

API_NAME="mangadex"
API_PATH=$(echo $API_NAME | tr '.' '/')
API_DOCS="api_docs"
API_VERSION="0.0.1"
#API_VERISON=$(grep -m 1 -oP 'version: \K(.*)$' api.yaml)

TMP="tmp"
TMP_CONFIG="tmp.json"

for cmd in curl java; do
  if ! hash $cmd 2>/dev/null; then
    echo "Command $cmd required, go install it first."
    exit 1
  fi
done

if [ ! -e $ARTIFACT ]; then
  curl -Lo $ARTIFACT $ARTIFACT_URL
fi

# create config
cat << EOF > $TMP_CONFIG
{
  "packageName": "$API_NAME",
  "packageVersion": "$API_VERSION"
}
EOF

java -jar $ARTIFACT generate -i api.yaml -o $TMP -l python -c $TMP_CONFIG

# move docs to its own folder
for folder in $API_DOCS $API_PATH; do
  if [ -d $folder ]; then
    rm -r $folder
  fi
done

mkdir $API_DOCS

mv $TMP/{docs,README.md} $API_DOCS
mv $TMP/$API_NAME $API_PATH

rm -r $TMP
rm $TMP_CONFIG

###########
# PATCHES #
###########
# Some parts of the generated code need to be monkey-patched for it to run in the first place.

# Add version string
cat << EOF >> $API_PATH/__init__.py

__version__ = "$API_VERSION"
EOF

# Add 'Object' as a vaild native type (should be lowercase 'object')
# otherwise an AttributeError is raised
cat << "EOF" >> $API_PATH/api_client.py

ApiClient.NATIVE_TYPES_MAPPING["Object"] = object
EOF
