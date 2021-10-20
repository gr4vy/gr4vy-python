from openapi_client.api import payment_options_api
import time
import openapi_client
from openapi_client.api import payment_options_api
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from openapi_client.model.error400_bad_request import Error400BadRequest
from pprint import pprint


class gr4vyPaymentOptions(payment_options_api.PaymentOptionsApi):
    def __init__(self, client):
        super().__init__(client)
    
    def listPaymentOptions(self, **kwargs):
        try:
            # List payment options
            api_response = self.list_payment_options(**kwargs)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling PaymentOptionsApi->list_payment_options: %s\n" % e)
