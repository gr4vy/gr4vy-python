import api.openapi_client
from api.openapi_client.api import payment_method_tokens_api
from pprint import pprint

class gr4vyPaymentMethodTokens(payment_method_tokens_api.gr4vy_PaymentMethodTokensApi):
    def __init__(self, client):
        super().__init__(client)
    
    def listPaymentMethodTokens(self, payment_method_id):
        try:
            # List payment method tokens
            api_response = self.list_payment_method_tokens(payment_method_id)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentMethodTokensApi->list_payment_method_tokens: %s\n" % e)