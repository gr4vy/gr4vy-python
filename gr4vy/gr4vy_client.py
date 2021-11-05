import base64
import json
import sys
import textwrap
import uuid
from datetime import datetime, timedelta, timezone
from os import environ

import cryptography.hazmat.primitives.asymmetric.ec as ec
import cryptography.hazmat.primitives.hashes as hashes
import cryptography.hazmat.primitives.serialization as serialization
import jose.jwk
from jwt import api_jwt
from pem import parse_file

from gr4vy.gr4vy_api.openapi_client import ApiClient, Configuration
from gr4vy.sdk_Buyers import gr4vyBuyers
from gr4vy.sdk_PaymentMethods import gr4vyPaymentMethods
from gr4vy.sdk_PaymentMethodTokens import gr4vyPaymentMethodTokens
from gr4vy.sdk_PaymentOptions import gr4vyPaymentOptions
from gr4vy.sdk_PaymentServiceDefinitions import gr4vyPaymentServiceDefinitions
from gr4vy.sdk_PaymentServices import gr4vyPaymentServices
from gr4vy.sdk_Transactions import gr4vyTransactions

VERSION = 0.1
PYTHON_VERSION = "{}.{}.{}".format(
    sys.version_info[0], sys.version_info[1], sys.version_info[2]
)


class Gr4vyClient:
    def __init__(self, gr4vyId, private_key_file):
        self.gr4vyId = gr4vyId
        self.private_key_file = private_key_file
        self.GenerateToken()
        self.CreateConfiguration()
        self.CreateClient()

    def private_key_file_to_string(self):
        if environ.get("PRIVATE_KEY") is not None:
            private_key_string = environ.get("PRIVATE_KEY")
        else:
            private_key_string = str(parse_file(self.private_key_file)[0])
        private_key_pem = textwrap.dedent(private_key_string).encode()

        private_pem = serialization.load_pem_private_key(private_key_pem, password=None)

        jwk = jose.jwk.construct(private_pem, algorithm="ES512").to_dict()

        kid = str(self.thumbprint(jwk))
        return private_key_string, kid

    def GenerateToken(self, scopes=["*.read", "*.write"], embed_data=None):
        private_key, kid = self.private_key_file_to_string()
        data = {
            "iss": "Gr4vy SDK {} - {}".format(VERSION, PYTHON_VERSION),
            "nbf": datetime.now(tz=timezone.utc),
            "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=3000),
            "jti": str(uuid.uuid4()),
            "scopes": scopes,
        }
        if embed_data:
            data["embed"] = embed_data
        self.token = api_jwt.encode(
            data, private_key, algorithm="ES512", headers={"kid": kid}
        )
        return self.token

    def GenerateEmbedToken(self, embed_data):
        self.GenerateToken(embed_data=embed_data)
        return self.token

    def CreateConfiguration(self):
        if self.gr4vyId.endswith(".app"):
            host = self.gr4vyId
        else:
            host = "https://api.{}.gr4vy.app".format(self.gr4vyId)
        self.configuration = Configuration(access_token=self.token, host=host)

    def CreateClient(self):
        self.client = ApiClient(self.configuration)

    def GetBuyer(self, buyer_id):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            return api_instance.getBuyer(buyer_id)

    def ListBuyers(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            return api_instance.listBuyers(**kwargs)

    def AddBuyer(self, buyer_request):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            return api_instance.addBuyer(buyer_request)

    def UpdateBuyer(self, buyer_id, buyer_update):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            return api_instance.updateBuyer(buyer_id, buyer_update)

    def DeleteBuyer(self, buyer_id):
        with self.client as api_client:
            api_instance = gr4vyBuyers(api_client)
            return api_instance.delete_buyer(buyer_id)

    def GetPaymentMethod(self, payment_method_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            return api_instance.getPaymentMethod(payment_method_id)

    def ListBuyerPaymentMethods(self, buyer_id, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            return api_instance.listBuyerPaymentMethods(buyer_id=buyer_id, **kwargs)

    def ListPaymentMethods(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            return api_instance.listPaymentMethods()

    def StorePaymentMethod(self, payment_method_request):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            return api_instance.storePaymentMethod(
                payment_method_request=payment_method_request
            )

    def DeletePaymentMethod(self, payment_method_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethods(api_client)
            return api_instance.deletePaymentMethod(payment_method_id)

    def ListPaymentMethodTokens(self, payment_method_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentMethodTokens(api_client)
            return api_instance.listPaymentMethodTokens(payment_method_id)

    def ListPaymentOptions(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyPaymentOptions(api_client)
            return api_instance.listPaymentOptions(**kwargs)

    def GetPaymentServiceDefinition(self, payment_service_definition_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentServiceDefinitions(api_client)
            return api_instance.getPaymentServiceDefinition(
                payment_service_definition_id
            )

    def ListPaymentServiceDefintions(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyPaymentServiceDefinitions(api_client)
            return api_instance.listPaymentServiceDefintions(**kwargs)

    def ListPaymentServices(self, **kwargs):
        print(**kwargs)
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            return api_instance.listPaymentServices(**kwargs)

    def AddPaymentService(self, payment_service_request):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            return api_instance.addPaymentService(payment_service_request)

    def DeletePaymentService(self, payment_service_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            return api_instance.deletePaymentService(payment_service_id)

    def GetPaymentService(self, payment_service_id):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            return api_instance.getPaymentService(payment_service_id)

    def UpdatePaymentService(self, payment_service_id, payment_service_update):
        with self.client as api_client:
            api_instance = gr4vyPaymentServices(api_client)
            return api_instance.updatePaymentService(
                payment_service_id, payment_service_update=payment_service_update
            )

    def AuthorizeNewTransaction(self, transaction_request):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            return api_instance.authorizeNewTransaction(
                transaction_request=transaction_request
            )

    def CaptureTransaction(self, transaction_id, transaction_capture_request):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            return api_instance.captureTransaction(
                transaction_id, transaction_capture_request
            )

    def GetTransaction(self, transaction_id):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            return api_instance.getTransaction(transaction_id)

    def ListTransactions(self, **kwargs):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            return api_instance.listTransactions(**kwargs)

    def RefundTransaction(self, transaction_id, transaction_refund_request):
        with self.client as api_client:
            api_instance = gr4vyTransactions(api_client)
            return api_instance.refundTransaction(
                transaction_id=transaction_id,
                transaction_refund_request=transaction_refund_request,
            )

    def b64e(self, value: bytes) -> str:
        return base64.urlsafe_b64encode(value).decode("utf8").strip("=")

    def thumbprint(self, jwk: dict) -> str:
        claims = {k: v for k, v in jwk.items() if k in {"kty", "crv", "x", "y"}}

        json_claims = json.dumps(claims, separators=(",", ":"), sort_keys=True)

        digest = hashes.Hash(hashes.SHA256())
        digest.update(json_claims.encode("utf8"))

        return self.b64e(digest.finalize())


class Gr4vyClientWithBaseUrl(Gr4vyClient):
    def __init__(self, base_url, private_key):
        super().__init__(base_url, private_key)
