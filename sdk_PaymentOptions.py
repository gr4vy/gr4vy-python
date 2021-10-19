from api.openapi_client.api import payment_options_api
import time
import api.openapi_client
from api.openapi_client.api import payment_options_api
from api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from api.openapi_client.model.error400_bad_request import Error400BadRequest
from pprint import pprint


class gr4vyPaymentOptions(payment_options_api.PaymentOptionsApi):
    def __init__(self, client):
        super().__init__(client)
    
    def listPaymentOptions(self, country=None, currency=None, environment=None, locale=None):
        try:
            # List payment options
            api_response = self.list_payment_options(country=country, currency=currency, environment=environment, locale=locale)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentOptionsApi->list_payment_options: %s\n" % e)
