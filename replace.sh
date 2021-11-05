
var1="'billing_details': (object,),"
rep1="'billing_details': (BillingDetails, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/buyer.py

var1="class Buyer(ModelNormal):"
rep1="from gr4vy_python.gr4vy_api.openapi_client.model.billing_details import BillingDetails\nclass Buyer(ModelNormal):"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/buyer.py

var1="'buyer': (object,),"
rep1="'buyer': (Buyer, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/payment_method.py

var1="'buyer': (object,),"
rep1="'buyer': (Buyer, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/payment_method.py

var1="'method': (object,),"
rep1="'method': (str, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/payment_method.py

var1="'mode': (object,),"
rep1="'mode': (str, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/payment_method.py

var1="class PaymentMethod(ModelNormal):"
rep1="from gr4vy_python.gr4vy_api.openapi_client.model.buyer import Buyer\nclass PaymentMethod(ModelNormal):"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/payment_method.py

var1="'id': (str,),"
rep1="'id': (str, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/payment_method_token.py

var1="'token': (str,),"
rep1="'token': (str, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/payment_method_token.py

var1="'payment_service': (object,),"
rep1="'payment_service': (PaymentService, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/payment_method_token.py

var1="class PaymentMethodToken(ModelNormal):"
rep1="from gr4vy_python.gr4vy_api.openapi_client.model.payment_service import PaymentService\nclass PaymentMethodToken(ModelNormal):"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/payment_method_token.py

var1="'mode': (str,),"
rep1="'mode': (str, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/payment_service_definition.py

var1="'buyer': (object,),"
rep1="'buyer': (Buyer, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/transaction.py

var1="'payment_method': (object,),"
rep1="'payment_method': (PaymentMethod, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/transaction.py

var1="'payment_service': (object,),"
rep1="'payment_service': (PaymentService, none_type),"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/transaction.py

var1="class Transaction(ModelNormal):"
rep1="from gr4vy_python.gr4vy_api.openapi_client.model.payment_service import PaymentService\nfrom gr4vy_python.gr4vy_api.openapi_client.model.payment_method import PaymentMethod\nfrom gr4vy_python.gr4vy_api.openapi_client.model.buyer import Buyer\nclass Transaction(ModelNormal):"
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/transaction.py

var1='from openapi_client'
rep1='from gr4vy_python.gr4vy_api.openapi_client'
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/*.py

var1='from openapi_client.'
rep1='from gr4vy_python.gr4vy_api.openapi_client.'
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/model/*.py

var1='from openapi_client.'
rep1='from gr4vy_python.gr4vy_api.openapi_client.'
sed -i '' "s/$var1/$rep1/g" ./gr4vy_python/gr4vy_api/openapi_client/api/*.py
