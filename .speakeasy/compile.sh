# #!/usr/bin/env bash

# // this doesn't work for the Speakeasy pyton SDK (yet)

# # Update code samples to use the global syntax
# if [[ "$OSTYPE" == "darwin"* ]]; then
#     find . -type f -name '*.md' | xargs sed -i '' '/^    server="sandbox"/d'
#     find . -type f -name '*.md' | xargs sed -i '' '/^    id="<id>"/d'
#     find . -type f -name '*.md' | xargs sed -i '' 's/^bearer_auth=os\.getenv("GR4VY_BEARER_AUTH", ""),/id="example",\nserver="sandbox",\nbearer_auth=auth\.with_token(open("\.\/private_key\.pem")\.read(), expires_in=1),/g'
#     find . -type f -name '*.md' | xargs sed -i '' 's/^  bearer_auth=os\.getenv("GR4VY_BEARER_AUTH", ""),/  id="example",\n  server="sandbox",\n  bearer_auth=auth\.with_token(open("\.\/private_key\.pem")\.read(), expires_in=1),/g'
#     find . -type f -name '*.md' | xargs sed -i '' 's/^    bearer_auth=os\.getenv("GR4VY_BEARER_AUTH", ""),/    id="example",\n    server="sandbox",\n    bearer_auth=auth\.with_token(open("\.\/private_key\.pem")\.read(), expires_in=1),/g'
#     find . -type f -name '*.md' | xargs sed -i '' 's/^      bearer_auth=os\.getenv("GR4VY_BEARER_AUTH", ""),/      id="example",\n      server="sandbox",\n      bearer_auth=auth\.with_token(open("\.\/private_key\.pem")\.read(), expires_in=1),/g'
#     find . -type f -name '*.md' | xargs sed -i '' 's/from gr4vy import Gr4vy$/from gr4vy import Gr4vy, auth/g'
# else
#     find . -type f -name '*.md' | xargs sed -i '/^    server="sandbox"/d'
#     find . -type f -name '*.md' | xargs sed -i '/^    id="<id>"/d'
#     find . -type f -name '*.md' | xargs sed -i 's/^bearer_auth=os\.getenv("GR4VY_BEARER_AUTH", ""),/id="example",\nserver="sandbox",\nbearer_auth=auth\.with_token(open("\.\/private_key\.pem")\.read(), expires_in=1),/g'
#     find . -type f -name '*.md' | xargs sed -i 's/^  bearer_auth=os\.getenv("GR4VY_BEARER_AUTH", ""),/  id="example",\n  server="sandbox",\n  bearer_auth=auth\.with_token(open("\.\/private_key\.pem")\.read(), expires_in=1),/g'
#     find . -type f -name '*.md' | xargs sed -i 's/^    bearer_auth=os\.getenv("GR4VY_BEARER_AUTH", ""),/    id="example",\n    server="sandbox",\n    bearer_auth=auth\.with_token(open("\.\/private_key\.pem")\.read(), expires_in=1),/g'
#     find . -type f -name '*.md' | xargs sed -i 's/^      bearer_auth=os\.getenv("GR4VY_BEARER_AUTH", ""),/      id="example",\n      server="sandbox",\n      bearer_auth=auth\.with_token(open("\.\/private_key\.pem")\.read(), expires_in=1),/g'
#     find . -type f -name '*.md' | xargs sed -i 's/from gr4vy import Gr4vy$/from gr4vy import Gr4vy, auth/g'
# fi
