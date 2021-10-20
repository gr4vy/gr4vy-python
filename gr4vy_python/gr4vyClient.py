from jwt import api_jwt
import uuid
from datetime import datetime, timezone, timedelta
import sys
from pem import parse_file

from .sdk_Buyers import gr4vyBuyers
from .sdk_PaymentMethods import gr4vyPaymentMethods
from .sdk_PaymentMethodTokens import gr4vyPaymentMethodTokens
from .sdk_PaymentOptions import gr4vyPaymentOptions
from .sdk_PaymentServiceDefinitions import gr4vyPaymentServiceDefinitions
from .sdk_PaymentServices import gr4vyPaymentServices
from .sdk_Transactions import gr4vyTransactions

from openapi_client import Configuration, ApiClient

from openapi_client.model.payment_service_update import PaymentServiceUpdate
from openapi_client.model.payment_service_update_fields import PaymentServiceUpdateFields
from openapi_client.model.payment_service_request import PaymentServiceRequest
from openapi_client.model.payment_method import PaymentMethod
from openapi_client.model.buyer_request import BuyerRequest
from openapi_client.model.billing_details import BillingDetails
from openapi_client.model.buyer_update import BuyerUpdate
from openapi_client.model.transaction_request import TransactionRequest
from openapi_client.model.transaction_capture_request import TransactionCaptureRequest
from openapi_client.model.transaction_refund_request import TransactionRefundRequest



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
        self.token = api_jwt.encode(data, private_key, algorithm="ES512", headers={"kid": kid})
    
    def generate_embed_token(self, scope, embed_data):
        self.generate_token(self, scope, embed_data)

    def createConfiguration(self):
        self.configuration = Configuration(
                            access_token = self.token,
                            host = 'https://api.{}.gr4vy.app'.format(self.gr4vyId)
                            )

    def createClient(self):
        self.client = ApiClient(self.configuration)
    
    def getBuyer(self, buyer_id):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            api_instance.getBuyer(buyer_id)
    
    def listBuyers(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            api_instance.listBuyers(**kwargs)

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
    
    def listBuyerPaymentMethods(self, buyer_id, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            api_instance.listBuyerPaymentMethods(buyer_id=buyer_id, **kwargs)

    def listPaymentMethods(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            api_instance.listPaymentMethods(**kwargs)

    def storePaymentMethod(self, payment_method):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            api_instance.storePaymentMethod(payment_method=payment_method)

    def deletePaymentMethod(self, payment_method_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            api_instance.deletePaymentMethod(payment_method_id)

    def listPaymentMethodTokens(self, payment_method_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethodTokens(api_client)
            api_instance.listPaymentMethodTokens(payment_method_id)

    def listPaymentOptions(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyPaymentOptions(api_client)
            api_instance.listPaymentOptions(**kwargs)

    def getPaymentServiceDefinition(self, payment_service_definition_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentOptions(api_client)
            api_instance.getPaymentServiceDefinition(payment_service_definition_id)

    def listPaymentServiceDefintions(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyPaymentServiceDefinitions(api_client)
            api_instance.listPaymentServiceDefintions(**kwargs)

    def listPaymentServices(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            api_instance.listPaymentServices(**kwargs)

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

    def updatePaymentService(self, payment_service_id, payment_service_update):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            api_instance.updatePaymentService(payment_service_id, payment_service_update=payment_service_update)

    def authorizeNewTransaction(self, transaction_request):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            api_instance.authorizeNewTransaction(transaction_request = transaction_request)

    def captureTransaction(self, transaction_id, transaction_capture_request):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            api_instance.captureTransaction(transaction_id, transaction_capture_request)

    def getTransaction(self,transaction_id):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            api_instance.getTransaction(transaction_id, transaction_id)

    def listTransactions(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            api_instance.listTransactions(**kwargs)
   
    def refundTransaction(self, transaction_id, transaction_refund_request):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            api_instance.refundTransaction(transaction_id, transaction_refund_request)