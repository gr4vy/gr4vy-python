import time
from pprint import pprint

import gr4vy.gr4vy_api.openapi_client
from gr4vy.gr4vy_api.openapi_client.api import payment_options_api
from gr4vy.gr4vy_api.openapi_client.model.error400_bad_request import Error400BadRequest
from gr4vy.gr4vy_api.openapi_client.model.error401_unauthorized import (
    Error401Unauthorized,
)


class gr4vyPaymentOptions(payment_options_api.PaymentOptionsApi):
    def __init__(self, client):
        super().__init__(client)

    def listPaymentOptions(self, **kwargs):
        try:
            # List payment options
            api_response = self.list_payment_options(**kwargs)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling PaymentOptionsApi->list_payment_options: %s\n"
                % e
            )
