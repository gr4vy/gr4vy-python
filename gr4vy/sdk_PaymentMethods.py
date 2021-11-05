import time
from pprint import pprint

import gr4vy.gr4vy_api.openapi_client
from gr4vy.gr4vy_api.openapi_client.api import payment_methods_api
from gr4vy.gr4vy_api.openapi_client.model.error401_unauthorized import (
    Error401Unauthorized,
)
from gr4vy.gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from gr4vy.gr4vy_api.openapi_client.model.payment_method import PaymentMethod


class gr4vyPaymentMethods(payment_methods_api.PaymentMethodsApi):
    def __init__(self, client):
        super().__init__(client)

    def deletePaymentMethod(self, payment_method_id):
        try:
            # Delete payment method
            self.delete_payment_method(payment_method_id)
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentMethodsApi->delete_payment_method: %s\n"
                % e
            )

    def getPaymentMethod(self, payment_method_id):
        try:
            # Get stored payment method
            api_response = self.get_payment_method(payment_method_id)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentMethodsApi->get_payment_method: %s\n" % e
            )

    def storePaymentMethod(self, payment_method_request=None):
        try:
            # New payment method
            api_response = self.store_payment_method(
                payment_method_request=payment_method_request
            )
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentMethodsApi->store_payment_method: %s\n"
                % e
            )

    def listBuyerPaymentMethods(self, buyer_id, **kwargs):
        try:
            # List stored payment methods for a buyer
            api_response = self.list_buyer_payment_methods(buyer_id=buyer_id, **kwargs)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentMethodsApi->list_buyer_payment_methods: %s\n"
                % e
            )

    def listPaymentMethods(self, **kwargs):
        try:
            # List payment methods
            api_response = self.list_payment_methods(**kwargs)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentMethodsApi->list_payment_methods: %s\n"
                % e
            )
