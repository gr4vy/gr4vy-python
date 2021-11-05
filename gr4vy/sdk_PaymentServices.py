from pprint import pprint

import gr4vy.gr4vy_api.openapi_client
from gr4vy.gr4vy_api.openapi_client.api import payment_services_api


class gr4vyPaymentServices(payment_services_api.PaymentServicesApi):
    def __init__(self, client):
        super().__init__(client)

    def listPaymentServices(self, **kwargs):
        try:
            # List payment services
            api_response = self.list_payment_services(**kwargs)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentServicesApi->list_payment_services: %s\n"
                % e
            )

    def addPaymentService(self, payment_service_request):
        try:
            # New payment service
            api_response = self.add_payment_service(
                payment_service_request=payment_service_request
            )
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentServicesApi->add_payment_service: %s\n"
                % e
            )

    def deletePaymentService(self, payment_service_id):
        try:
            # Delete payment service
            self.delete_payment_service(payment_service_id)
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentServicesApi->delete_payment_service: %s\n"
                % e
            )

    def getPaymentService(self, payment_service_id):
        try:
            # Get payment service
            api_response = self.get_payment_service(payment_service_id)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentServicesApi->get_payment_service: %s\n"
                % e
            )

    def updatePaymentService(self, payment_service_id, payment_service_update):
        try:
            # Update payment service

            api_response = self.update_payment_service(
                payment_service_id=payment_service_id,
                payment_service_update=payment_service_update,
            )
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentServicesApi->update_payment_service: %s\n"
                % e
            )
