from gr4vy_python.gr4vy_api.openapi_client.api import payment_options_api
import time
import gr4vy_python.gr4vy_api.openapi_client
from gr4vy_python.gr4vy_api.openapi_client.api import payment_options_api
from gr4vy_python.gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from gr4vy_python.gr4vy_api.openapi_client.model.error400_bad_request import Error400BadRequest
from pprint import pprint


class gr4vyPaymentOptions(payment_options_api.PaymentOptionsApi):
    def __init__(self, client):
        super().__init__(client)
    
    def listPaymentOptions(self, **kwargs):
        try:
            # List payment options
            api_response = self.list_payment_options(**kwargs)
            return api_response
        except gr4vy_python.gr4vy_api.openapi_client.ApiException as e:
            print("Exception when calling PaymentOptionsApi->list_payment_options: %s\n" % e)
