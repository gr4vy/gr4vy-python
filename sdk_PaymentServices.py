import api.openapi_client
from api.openapi_client.api import payment_services_api
from pprint import pprint

class gr4vyPaymentServices(payment_services_api.PaymentServicesApi):
    def __init__(client):
        super().__init__(client)

    def listPaymentServices(self, limit=None, cursor=None, method=None, environment=None):
        try:
            # List payment services
            api_response = self.list_payment_services(limit=limit, cursor=cursor, method=method, environment=environment)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentServicesApi->list_payment_services: %s\n" % e)
    
    def addPaymentService(self, payment_service_request):
        try:
            # New payment service
            api_response = self.add_payment_service(payment_service_request=payment_service_request)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentServicesApi->add_payment_service: %s\n" % e)

    def deletePaymentService(self, payment_service_id):
        try:
            # Delete payment service
            self.delete_payment_service(payment_service_id)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentServicesApi->delete_payment_service: %s\n" % e)
    
    def getPaymentService(self, payment_service_id):
        try:
            # Get payment service
            api_response = self.get_payment_service(payment_service_id)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentServicesApi->get_payment_service: %s\n" % e)

    def updatePaymentService(self, payment_service_id, payment_service_update=None):
        try:
            # Update payment service
            api_response = self.update_payment_service(payment_service_id, payment_service_update=payment_service_update)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling PaymentServicesApi->update_payment_service: %s\n" % e)