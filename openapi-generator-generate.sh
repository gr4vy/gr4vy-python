#!/bin/bash

#delete previous api directory
rm -rf api
docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i https://raw.githubusercontent.com/gr4vy/gr4vy-openapi/openapi-3.0/openapi.v1.json \
  -g python \
  --git-user-id gr4vy \
  --git-repo-id gr4vy-python \
  -o /local/api