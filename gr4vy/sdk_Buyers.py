from pprint import pprint

import gr4vy.gr4vy_api.openapi_client
from gr4vy.gr4vy_api.openapi_client.api import buyers_api
from gr4vy.gr4vy_api.openapi_client.model.error401_unauthorized import (
    Error401Unauthorized,
)


class gr4vyBuyers(buyers_api.BuyersApi):
    def __init__(self, client):
        super().__init__(client)

    def listBuyers(self, **kwargs):
        try:
            # List buyers
            api_response = self.list_buyers(**kwargs)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print("Exception when calling BuyersApi->list_buyers: %s\n" % e)

    def addBuyer(self, buyer_request):
        try:
            # New buyer
            api_response = self.add_buyer(buyer_request=buyer_request)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print("Exception when calling BuyersApi->add_buyer: %s\n" % e)

    def getBuyer(self, buyer_id):
        try:
            # Get buyer
            api_response = self.get_buyer(buyer_id)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print("Exception when calling BuyersApi->get_buyer: %s\n" % e)

    def updateBuyer(self, buyer_id, buyer_update):
        try:
            # Update buyer
            api_response = self.update_buyer(buyer_id, buyer_update=buyer_update)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print("Exception when calling BuyersApi->update_buyer: %s\n" % e)

    def deleteBuyer(self, buyer_id):
        try:
            # Delete buyer
            api_response = self.delete_buyer(buyer_id)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)
