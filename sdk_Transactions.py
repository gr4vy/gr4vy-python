import time
import api.openapi_client
from api.openapi_client.api import transactions_api
from pprint import pprint

class gr4vyTransactions(transactions_api.TransactionsApi):
    def __init__(client):
        super().__init__(client)

    def authorizeNewTransaction(self, transaction_request = None):
        try:
            # New transaction
            api_response = self.authorize_new_transaction(transaction_request=transaction_request)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling TransactionsApi->authorize_new_transaction: %s\n" % e)

    def captureTransaction(self, transaction_id, transaction_capture_request = None):
        try:
            # Capture transaction
            api_response = self.capture_transaction(transaction_id, transaction_capture_request=transaction_capture_request)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling TransactionsApi->capture_transaction: %s\n" % e)

    def getTransaction(self,transaction_id):
        try:
            # Get transaction
            api_response = self.get_transaction(transaction_id)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)

    def listTransactions(self, search=None, transaction_status=None, buyer_id=None, buyer_external_identifier=None, before_created_at=None, after_created_at=after_created_at, before_updated_at=before_updated_at, after_updated_at=None, limit=None, cursor=None):
        try:
            # List transactions
            api_response = self.list_transactions(search=search, transaction_status=transaction_status, buyer_id=buyer_id, buyer_external_identifier=buyer_external_identifier, before_created_at=before_created_at, after_created_at=after_created_at, before_updated_at=before_updated_at, after_updated_at=after_updated_at, limit=limit, cursor=cursor)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)

    def refundTransaction(self, transaction_id, transaction_refund_request):
        try:
            # Refund or void transactions
            api_response = self.refund_transaction(transaction_id, transaction_refund_request=transaction_refund_request)
            pprint(api_response)
        except api.openapi_client.ApiException as e:
            print("Exception when calling TransactionsApi->refund_transaction: %s\n" % e)
