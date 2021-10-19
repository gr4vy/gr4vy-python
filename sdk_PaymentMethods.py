import time
import api.openapi_client
from api.openapi_client.api import payment_methods_api
from api.openapi_client.model.error404_not_found import Error404NotFound
from api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from api.openapi_client.model.payment_method import PaymentMethod


from pprint import pprint

class gr4vyPaymentMethods(payment_methods_api.PaymentMethodsApi):
    def __init__(self, client):
        super().__init__(client)
    
    def deletePaymentMethod(self, payment_method_id):
        try:
            # Delete payment method
            self.delete_payment_method(payment_method_id)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentMethodsApi->delete_payment_method: %s\n" % e)

    def getPaymentMethod(self, payment_method_id):
        try:
            # Get stored payment method
            api_response = self.get_payment_method(payment_method_id)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentMethodsApi->get_payment_method: %s\n" % e)

    #TO DO
    def storePaymentMethod(self, payment_method=None):
        try:
            # New payment method
            api_response = self.store_payment_method(payment_method)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentMethodsApi->store_payment_method: %s\n" % e)

    def listBuyerPaymentMethods(self, buyer_id=None, buyer_external_identifier=None, country=None, currency=None, environment=None):
        try:
            # List stored payment methods for a buyer
            api_response = self.list_buyer_payment_methods(buyer_id=buyer_id, buyer_external_identifier=buyer_external_identifier, country=country, currency=currency, environment=environment)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentMethodsApi->list_buyer_payment_methods: %s\n" % e)

    def listPaymentMethods(self, environment=None, buyer_id=None, buyer_external_identifier=None, limit=None, cursor=None):
        try:
            # List payment methods
            api_response = self.list_payment_methods(environment=environment, buyer_id=buyer_id, buyer_external_identifier=buyer_external_identifier, limit=limit, cursor=cursor)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentMethodsApi->list_payment_methods: %s\n" % e)
