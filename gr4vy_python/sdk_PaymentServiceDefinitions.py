from openapi_client.api import payment_service_definitions_api
import time
import openapi_client
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint

class gr4vyPaymentServiceDefinitions(payment_service_definitions_api.PaymentServiceDefinitionsApi):
    def __init__(self, client):
        super().__init__(client)
    
    def getPaymentServiceDefinition(self, payment_service_definition_id):
        try:
            # Get payment service definition
            api_response = self.get_payment_service_definition(payment_service_definition_id)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling PaymentServiceDefinitionsApi->get_payment_service_definition: %s\n" % e)

    def listPaymentServiceDefintions(self, **kwargs):
        try:
            # List payment service definitions
            api_response = self.list_payment_service_definitions(**kwargs)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling PaymentServiceDefinitionsApi->list_payment_service_definitions: %s\n" % e)
