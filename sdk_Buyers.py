import api.openapi_client
from api.openapi_client.api import buyers_api
from api.openapi_client.model.buyer_request import BuyerRequest
from api.openapi_client.model.billing_details import BillingDetails
from api.openapi_client.model.buyer_update import BuyerUpdate
from pprint import pprint
from api.openapi_client.model.error401_unauthorized import Error401Unauthorized


class gr4vyBuyers(buyers_api.BuyersApi):
    def __init__(self, client):
        super().__init__(client)
    
    def listBuyers(self, search = '', limit = None, cursor = ''):
        try:
            # List buyers
            api_response = self.list_buyers(search=search, limit=limit, cursor=cursor)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling BuyersApi->list_buyers: %s\n" % e)
    
    def addBuyer(self, buyer_request):
        try:
            # New buyer
            api_response = self.add_buyer(buyer_request=buyer_request)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling BuyersApi->add_buyer: %s\n" % e)
    
    def getBuyer(self, buyer_id):
        try:
            # Get buyer
            api_response = self.get_buyer(buyer_id)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling BuyersApi->get_buyer: %s\n" % e)

    def updateBuyer(self, buyer_id, buyer_update):
        try:
            # Update buyer
            api_response = self.update_buyer(buyer_id, buyer_update=buyer_update)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling BuyersApi->update_buyer: %s\n" % e)
    
    def deleteBuyer(self, buyer_id):
        try:
            # Delete buyer
            self.delete_buyer(buyer_id)
        except api.openapi_client.ApiException as e:
            print("Exception when calling BuyersApi->delete_buyer: %s\n" % e)