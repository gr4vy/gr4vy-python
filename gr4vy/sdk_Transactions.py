from pprint import pprint

import gr4vy.gr4vy_api.openapi_client
from gr4vy.gr4vy_api.openapi_client.api import transactions_api


class gr4vyTransactions(transactions_api.TransactionsApi):
    def __init__(self, client):
        super().__init__(client)

    def authorizeNewTransaction(self, transaction_request):
        try:
            # New transaction
            api_response = self.authorize_new_transaction(
                transaction_request=transaction_request
            )
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling TransactionsApi->authorize_new_transaction: %s\n"
                % e
            )

    def captureTransaction(self, transaction_id, transaction_capture_request):
        try:
            # Capture transaction
            api_response = self.capture_transaction(
                transaction_id, transaction_capture_request=transaction_capture_request
            )
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling TransactionsApi->capture_transaction: %s\n" % e
            )

    def getTransaction(self, transaction_id):
        try:
            # Get transaction
            api_response = self.get_transaction(transaction_id)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)

    def listTransactions(self, **kwargs):
        try:
            # List transactions
            api_response = self.list_transactions(**kwargs)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)

    def refundTransaction(self, transaction_id, **kwargs):
        try:
            # Refund or void transactions
            api_response = self.refund_transaction(transaction_id, **kwargs)
            return api_response
        except gr4vy.gr4vy_api.openapi_client.ApiException as e:
            print(
                "Exception when calling TransactionsApi->refund_transaction: %s\n" % e
            )
