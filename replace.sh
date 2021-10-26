var1='from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE'
rep1=''
sed -i '' "s/$var1/$rep1/g" ./gr4vy_api/openapi_client/api/*_api.py

var1='unknown_base_type'
rep1=''
sed -i '' "s/$var1/$rep1/g" ./gr4vy_api/openapi_client/api/*_api.py

var1='UNKNOWN_BASE_TYPE,'
rep1=''
sed -i '' "s/$var1/$rep1/g" ./gr4vy_api/openapi_client/api/*_api.py

var1='from openapi_client.'
rep1='from gr4vy_api.openapi_client.'
sed -i '' "s/$var1/$rep1/g" ./gr4vy_api/openapi_client/*.py

var1='from openapi_client.'
rep1='from gr4vy_api.openapi_client.'
sed -i '' "s/$var1/$rep1/g" ./gr4vy_api/openapi_client/model/*.py

var1='from openapi_client.'
rep1='from gr4vy_api.openapi_client.'
sed -i '' "s/$var1/$rep1/g" ./gr4vy_api/openapi_client/api/*.py
