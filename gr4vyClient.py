import jwt
import uuid
from datetime import datetime, timezone, timedelta
import sys
from pem import parse_file

import api.openapi_client

from sdk_Buyers import gr4vyBuyers
from sdk_PaymentMethods import gr4vyPaymentMethods
from sdk_PaymentMethodTokens import gr4vyPaymentMethodTokens
from sdk_PaymentOptions import gr4vyPaymentOptions
from sdk_PaymentServiceDefinitions import gr4vyPaymentServiceDefinitions
from sdk_PaymentServices import gr4vyPaymentServices
from sdk_Transactions import gr4vyTransactions

from api.openapi_client.model.payment_service_update import PaymentServiceUpdate
from api.openapi_client.model.payment_service_update_fields import PaymentServiceUpdateFields
from api.openapi_client.model.payment_service_request import PaymentServiceRequest
from api.openapi_client.model.payment_method import PaymentMethod
from api.openapi_client.model.buyer_request import BuyerRequest
from api.openapi_client.model.billing_details import BillingDetails
from api.openapi_client.model.buyer_update import BuyerUpdate
from api.openapi_client.model.transaction_request import TransactionRequest
from api.openapi_client.model.transaction_capture_request import TransactionCaptureRequest
from api.openapi_client.model.transaction_refund_request import TransactionRefundRequest



VERSION = 0.1
PYTHON_VERSION = '{}.{}.{}'.format(sys.version_info[0], sys.version_info[1], sys.version_info[2])

class Gr4vyClient:
    def __init__(self, gr4vyId, private_key_file, scopes = ["*.read", "*.write"]):
        self.gr4vyId = gr4vyId
        self.private_key_file = private_key_file
        self.scopes = scopes
        self.generate_token(self.scopes)
        self.createConfiguration()
        self.createClient()

    def private_key_file_to_string(self):
        kid = 'JZQwKoE1CAx8Z33SSjy8vBKdB1fpmcGyLsDXSxsbgSg'
        return str(parse_file(self.private_key_file)[0]), kid

    def generate_token(self, scopes, embed_data = None):
        private_key, kid = self.private_key_file_to_string()
        data = {"iss": "Gr4vy SDK {} - {}".format(VERSION, PYTHON_VERSION),
                "nbf": datetime.now(tz=timezone.utc),
                "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=3000),
                "jti": str(uuid.uuid4()),
                "scopes": scopes
                }
        if embed_data:
            data["embed"] = embed_data
        self.token = jwt.encode(data, private_key, algorithm="ES512", headers={"kid": kid})
    
    def generate_embed_token(self, scope, embed_data):
        self.generate_token(self, scope, embed_data)

    def createConfiguration(self):
        self.configuration = api.openapi_client.Configuration(
                            access_token = self.token,
                            host = 'https://api.{}.gr4vy.app'.format(self.gr4vyId)
                            )

    def createClient(self):
        self.client = api.openapi_client.ApiClient(self.configuration)
    
    def getBuyer(self, buyer_id):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            api_instance.getBuyer(buyer_id)
    
    def listBuyers(self, search = '', limit = None, cursor = ''):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            api_instance.listBuyers(search = search, limit = limit, cursor = cursor)

    def addBuyer(self, buyer_request):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            api_instance.addBuyer(buyer_request)

    def updateBuyer(self, buyer_id, buyer_update):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            api_instance.pdateBuyer(buyer_id, buyer_update)

    def getPaymentMethod(self, payment_method_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            api_instance.getPaymentMethod(payment_method_id)
    
    def listBuyerPaymentMethods(self, buyer_id=None, buyer_external_identifier=None, country=None, 
                                currency=None, environment=None):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            api_instance.listBuyerPaymentMethods(buyer_id=buyer_id, buyer_external_identifier=buyer_external_identifier, country=country, 
                                currency=currency, environment=environment)

    def listPaymentMethods(self, environment=None, buyer_id=None, buyer_external_identifier=None,
                            limit=None, cursor=None):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            api_instance.listPaymentMethods(environment=environment, buyer_id=buyer_id, buyer_external_identifier=buyer_external_identifier,
                            limit=limit, cursor=cursor)

    def storePaymentMethod(self, payment_method=None, unknown_base_type=None):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            api_instance.storePaymentMethod(payment_method=payment_method, unknown_base_type=unknown_base_type)

    def deletePaymentMethod(self, payment_method_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            api_instance.deletePaymentMethod(payment_method_id)

    def listPaymentMethodTokens(self, payment_method_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethodTokens(api_client)
            api_instance.listPaymentMethodTokens(payment_method_id)

    def listPaymentOptions(self, country=None, currency=None, environment=None, locale=None):
        with self.client as api_client:
            api_instance = gr4vyPaymentOptions(api_client)
            api_instance.listPaymentOptions(country=country, currency=currency, environment=environment, locale=locale)

    def getPaymentServiceDefinition(self, payment_service_definition_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentOptions(api_client)
            api_instance.getPaymentServiceDefinition(payment_service_definition_id)

    def listPaymentServiceDefintions(self, limit = None, cursor = None):
        with self.client as api_client:
            api_instance = gr4vyPaymentServiceDefinitions(api_client)
            api_instance.listPaymentServiceDefintions(limit = limit, cursor = cursor)

    def listPaymentServices(self, limit=None, cursor=None, method=None, environment=None):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            api_instance.listPaymentServices(limit=limit, cursor=cursor, method=method, environment=environment)

    def addPaymentService(self, payment_service_request):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            api_instance.addPaymentService(payment_service_request)

    def deletePaymentService(self, payment_service_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            api_instance.deletePaymentService(payment_service_id)

    def getPaymentService(self, payment_service_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            api_instance.getPaymentService(payment_service_id)

    def updatePaymentService(self, payment_service_id, payment_service_update=None):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            api_instance.updatePaymentService(payment_service_id, payment_service_update=payment_service_update)

    def authorizeNewTransaction(self, transaction_request = None):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            api_instance.authorizeNewTransaction(transaction_request = transaction_request)

    def captureTransaction(self, transaction_id, transaction_capture_request = None):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            api_instance.captureTransaction(transaction_id, transaction_capture_request = transaction_capture_request)


#Gr4vyClient_obj = Gr4vyClient("spider","private_key.pem")
#Gr4vyClient_obj.listBuyers('Phil Thomas')