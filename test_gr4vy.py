from gr4vy_python.gr4vy_api.openapi_client.model.buyer_request import BuyerRequest
from gr4vy_python.gr4vy_api.openapi_client.model.buyer_update import BuyerUpdate
from gr4vy_python.gr4vy_api.openapi_client.model.payment_method import PaymentMethod
from gr4vy_python.gr4vy_api.openapi_client.model.payment_service_request import PaymentServiceRequest
from gr4vy_python.gr4vy_api.openapi_client.model.payment_service_update import PaymentServiceUpdate
from gr4vy_python.gr4vy_api.openapi_client.model.transaction_capture_request import TransactionCaptureRequest
from gr4vy_python.gr4vy_api.openapi_client.model.transaction_refund_request import TransactionRefundRequest
from gr4vy_python.gr4vy_api.openapi_client.model.transaction_request import TransactionRequest
from gr4vy_python import Gr4vyClient
from gr4vy_python import Gr4vyClientWithBaseUrl

gr4vy_id = "spider"
private_key_location = "./private_key.pem"

client = Gr4vyClient(gr4vy_id,private_key_location)

# method = {
#   "method": "card",
#   "number": "4111111111111111",
#   "expiration_date": "11/25",
#   "security_code": "123"
# }
# payment_method = PaymentMethod(**method)
# payment_method_id = client.StorePaymentMethod(payment_method).id

# payment_service = {
# "id": "faaad066-30b4-4997-a438-242b0752d7e1",
# "type": "payment-service",
# "payment_service_definition_id": "stripe",
# "method": "card",
# "display_name": "Stripe",
# "status": "pending",
# "accepted_currencies": [
# "EUR"
# ],
# "accepted_countries": [
# "DE"
# ],
# "environment": "production"
# }

# payment_service_request = PaymentServiceRequest(**payment_service
# )

# payment_service_request = PaymentServiceRequest(**payment_service)
# payment_service_id = client.AddPaymentService(payment_service_request).id


# transaction_request = {
#   "amount": 1299,
#   "currency": "USD",
#   "payment_method": {
#     "method": "card",
#     "number": "4111111111111111",
#     "expiration_date": "11/25",
#     "security_code": "123",
#     "redirect_url": "https://example.com/callback"
#   }
# }

# transaction_request = TransactionRequest(**transaction_request)
# transaction_id = client.AuthorizeNewTransaction(transaction_request).id


def testCreateClient():
    assert client

def testGr4vyClientWithBaseUrl():
    assert Gr4vyClientWithBaseUrl("https://spider.gr4vy.app", "private_key.pem")

def testprivate_key_file_to_string():
    assert client.private_key_file_to_string()

def testGenerateToken():
    assert client.GenerateToken()

def testGenerateEmbedToken():
    buyer_id = client.ListBuyers()["items"][0]["id"]
    embed = {"amount": 1299,
            "currency": "USD",
            "buyerId": buyer_id,
            } 
    assert client.GenerateEmbedToken(embed)
'''
def testAddBuyer():
    buyer_request = BuyerRequest(display_name="Test")
    assert client.AddBuyer(buyer_request)
'''
def testGetBuyer():
    buyer_id = client.ListBuyers()["items"][0]["id"]
    assert client.GetBuyer(buyer_id)

def testListBuyers():
    assert client.ListBuyers()

def testUpdateBuyer():
    buyer_id = client.ListBuyers()["items"][0]["id"]
    buyer_update = BuyerUpdate()
    assert client.UpdateBuyer(buyer_id, buyer_update)

'''
def testDeleteBuyer():
    try:
        buyer_id = client.ListBuyers()["items"][0]
        client.DeleteBuyer(buyer_id)
    except KeyError:
        print("No buyer's to delete")
        assert False
'''
'''
def testGetPaymentMethod():
    assert client.GetPaymentMethod(payment_method_id)
'''
def testListBuyerPaymentMethods():
    buyer_id = client.ListBuyers()["items"][0]["id"]
    assert client.ListBuyerPaymentMethods(buyer_id)

def testListPaymentMethods():
    assert client.ListPaymentMethods()
'''
def testStorePaymentMethod():
    assert client.StorePaymentMethod(payment_method)

def testDeletePaymentMethod():
    assert client.DeletePaymentMethod(payment_method_id)
'''
def testListPaymentMethodTokens():
    payment_method_id = client.ListPaymentMethods()["items"][0]["id"]
    assert client.ListPaymentMethodTokens(payment_method_id)


def testListPaymentOptions():
    assert client.ListPaymentOptions()

def testGetPaymentServiceDefinition():
    payment_service_definition_id = client.ListPaymentServiceDefintions(limit=1)["items"][0]["id"]
    assert client.GetPaymentServiceDefinition(payment_service_definition_id)

def testListPaymentServiceDefintions():
    assert client.ListPaymentServiceDefintions()

def testListPaymentServices():
    assert client.ListPaymentServices()
'''
def testAddPaymentService():
    assert client.AddPaymentService(payment_service_request)
'''
def testGetPaymentService():
    payment_service_id = client.ListPaymentServices()["items"][0]["id"]
    assert client.GetPaymentService(payment_service_id)
'''
def testUpdatePaymentService():
    payment_service_update = PaymentServiceUpdate(payment_service)
    assert client.UpdatePaymentService(payment_service_update)

def testAuthorizeNewTransaction():
    assert client.AuthorizeNewTransaction(transaction_request)

def testCaptureTransaction():
    transaction_capture = {
        "amount": 1299,
        "currency": "USD"
    }
    transaction_capture_request = TransactionCaptureRequest(**transaction_capture)
    assert client.CaptureTransaction(transaction_id, transaction_capture_request)
'''
def testGetTransaction():
    transaction_id = client.ListTransactions()["items"][0]["id"]
    assert client.GetTransaction(transaction_id)

def testListTransactions():
    assert client.ListTransactions()
'''
def testRefundTransaction():
    transaction_id = client.ListTransactions()["items"][0]["id"]
    TransactionRefundRequest()
    assert client.RefundTransaction(transaction_id, )

def testDeletePaymentService():
    assert client.DeletePaymentService(payment_service_id)

def testDeletePaymentMethod():
    assert client.DeletePaymentMethod(payment_method_id)
'''
