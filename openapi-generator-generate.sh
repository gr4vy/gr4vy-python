#delete previous api directory
rm -rf gr4vy_api
rm -rf gr4vy/gr4vy_api
docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i https://raw.githubusercontent.com/gr4vy/gr4vy-openapi/sdks/openapi.v1.json \
  -g python \
  --git-user-id gr4vy \
  --git-repo-id gr4vy-python \
  -o /local/gr4vy/gr4vy_api \
  -c /local/.openapi-generator-config.json

sh replace.sh

