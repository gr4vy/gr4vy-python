
var1='from openapi_client'
rep1='from gr4vy_python.gr4vy_api.openapi_client'
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/*.py

var1='from openapi_client.'
rep1='from gr4vy_python.gr4vy_api.openapi_client.'
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/*.py

var1='from openapi_client.'
rep1='from gr4vy_python.gr4vy_api.openapi_client.'
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/api/*.py
