# api.openapi_client.TransactionsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_transaction**](TransactionsApi.md#approve_transaction) | **GET** /transactions/{transaction_id}/approve | Buyer approval callback
[**authorize_new_transaction**](TransactionsApi.md#authorize_new_transaction) | **POST** /transactions | New transaction
[**capture_transaction**](TransactionsApi.md#capture_transaction) | **POST** /transactions/{transaction_id}/capture | Capture transaction
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /transactions/{transaction_id} | Get transaction
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /transactions | List transactions
[**redirect_transaction_approval**](TransactionsApi.md#redirect_transaction_approval) | **GET** /transactions/approvals/{transaction_approval_token} | Redirect buyer to service
[**refund_transaction**](TransactionsApi.md#refund_transaction) | **POST** /transactions/{transaction_id}/refund | Refund or void transactions


# **approve_transaction**
> approve_transaction(transaction_id)

Buyer approval callback

Internal API used as a redirect endpoint for transactions that require buyer authorization.  For example, when a buyer tries to create a PayPal transaction, the buyer needs to be sent to PayPal, after which they are sent back to this endpoint upon completion.  This API applies any required updates for the transaction based on its query parameters and then redirects the browser back to the `redirect_url` specified when the payment method was first created.

### Example


```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import transactions_api
from gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)


# Enter a context with an instance of the API client
with api.openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.

    # example passing only required values which don't have defaults set
    try:
        # Buyer approval callback
        api_instance.approve_transaction(transaction_id)
    except api.openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->approve_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirects the browser back to the &#x60;redirect_url&#x60; specified when the transaction was first created. It appends the transaction&#39;s ID and status. |  * location - The URL to redirect the browser to. This is the &#x60;redirect_url&#x60; specified when the transaction was first created with some additional query parameters appended.  * &#x60;transaction_id&#x60; - The ID of the transaction * &#x60;transaction_status&#x60; - The current value of the   &#x60;status&#x60;  field of the transaction. <br>  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_new_transaction**
> Transaction authorize_new_transaction()

New transaction

Attempts to create an authorization for a payment method. In some cases it is not possible to create the authorization without redirecting the user for their authorization. In these cases the status is set to `buyer_approval_pending` and an `approval_url` is returned.  Additionally, this endpoint accepts a few additional fields that allow for simultaneous capturing and storage of the payment method.  * `store` - Use this field to store the payment method for future use. Not all payment methods support this feature. * `capture` - Use this method to also perform a capture of the transaction after it has been authorized. 

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import transactions_api
from gr4vy_api.openapi_client.model.transaction import Transaction
from gr4vy_api.openapi_client.model.transaction_request import TransactionRequest
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = api.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with api.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_request = TransactionRequest(
        amount=1299,
        currency="USD",
        payment_method=None,
        store=True,
        intent="capture",
        external_identifier="user-789123",
        environment="staging",
        three_d_secure_data=None,
    ) # TransactionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New transaction
        api_response = api_instance.authorize_new_transaction(transaction_request=transaction_request)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->authorize_new_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_request** | [**TransactionRequest**](TransactionRequest.md)|  | [optional]

### Return type

[**Transaction**](Transaction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the created transaction. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **capture_transaction**
> Transaction capture_transaction(transaction_id)

Capture transaction

Captures a previously authorized transaction.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import transactions_api
from gr4vy_api.openapi_client.model.transaction import Transaction
from gr4vy_api.openapi_client.model.transaction_capture_request import TransactionCaptureRequest
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = api.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with api.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.
    transaction_capture_request = TransactionCaptureRequest(
        amount=1299,
    ) # TransactionCaptureRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Capture transaction
        api_response = api_instance.capture_transaction(transaction_id)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->capture_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Capture transaction
        api_response = api_instance.capture_transaction(transaction_id, transaction_capture_request=transaction_capture_request)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->capture_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |
 **transaction_capture_request** | [**TransactionCaptureRequest**](TransactionCaptureRequest.md)|  | [optional]

### Return type

[**Transaction**](Transaction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the captured transaction. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found or has not yet been created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> Transaction get_transaction(transaction_id)

Get transaction

Get information about a transaction.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import transactions_api
from gr4vy_api.openapi_client.model.transaction import Transaction
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = api.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with api.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.

    # example passing only required values which don't have defaults set
    try:
        # Get transaction
        api_response = api_instance.get_transaction(transaction_id)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a transaction resource. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found or has not yet been created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> Transactions list_transactions()

List transactions

Lists all transactions for an account. Sorted by last `updated_at` status.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import transactions_api
from gr4vy_api.openapi_client.model.transactions import Transactions
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = api.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with api.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    search = "be828248-56de-481e-a580-44b6e1d4df81" # str | Filters the transactions to only the items for which the `id` or `external_identifier` matches this value. This field allows for a partial match, matching any transaction for which either of the fields partially or completely matches. (optional)
    transaction_status = "capture_succeeded" # str | Filters the results to only the transactions for which the `status` matches this value. (optional)
    buyer_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | Filters the results to only the items for which the `buyer` has an `id` that matches this value. (optional)
    buyer_external_identifier = "user-12345" # str | Filters the results to only the items for which the `buyer` has an `external_identifier` that matches this value. (optional)
    before_created_at = "2012-12-12T10:53:43+00:00" # str | Filters the results to only transactions created before this ISO date-time string. (optional)
    after_created_at = "2012-12-12T10:53:43+00:00" # str | Filters the results to only transactions created after this ISO date-time string. (optional)
    before_updated_at = "2012-12-12T10:53:43+00:00" # str | Filters the results to only transactions last updated before this ISO date-time string. (optional)
    after_updated_at = "2012-12-12T10:53:43+00:00" # str | Filters the results to only transactions last updated after this ISO date-time string. (optional)
    environment = "staging" # str | Filters the results to only the items available in this environment. (optional) if omitted the server will use the default value of "production"
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transactions
        api_response = api_instance.list_transactions(search=search, transaction_status=transaction_status, buyer_id=buyer_id, buyer_external_identifier=buyer_external_identifier, before_created_at=before_created_at, after_created_at=after_created_at, before_updated_at=before_updated_at, after_updated_at=after_updated_at, environment=environment, limit=limit, cursor=cursor)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Filters the transactions to only the items for which the &#x60;id&#x60; or &#x60;external_identifier&#x60; matches this value. This field allows for a partial match, matching any transaction for which either of the fields partially or completely matches. | [optional]
 **transaction_status** | **str**| Filters the results to only the transactions for which the &#x60;status&#x60; matches this value. | [optional]
 **buyer_id** | **str**| Filters the results to only the items for which the &#x60;buyer&#x60; has an &#x60;id&#x60; that matches this value. | [optional]
 **buyer_external_identifier** | **str**| Filters the results to only the items for which the &#x60;buyer&#x60; has an &#x60;external_identifier&#x60; that matches this value. | [optional]
 **before_created_at** | **str**| Filters the results to only transactions created before this ISO date-time string. | [optional]
 **after_created_at** | **str**| Filters the results to only transactions created after this ISO date-time string. | [optional]
 **before_updated_at** | **str**| Filters the results to only transactions last updated before this ISO date-time string. | [optional]
 **after_updated_at** | **str**| Filters the results to only transactions last updated after this ISO date-time string. | [optional]
 **environment** | **str**| Filters the results to only the items available in this environment. | [optional] if omitted the server will use the default value of "production"
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]

### Return type

[**Transactions**](Transactions.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of transactions for an account. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redirect_transaction_approval**
> redirect_transaction_approval(transaction_approval_token)

Redirect buyer to service

Redirect a buyer to an alternative payment provider to approve their transaction. This is mainly used with providers like GoCardless and Klarna to redirect a buyer to their sites.

### Example


```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import transactions_api
from gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)


# Enter a context with an instance of the API client
with api.openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_approval_token = "NDY5NzNlOWQtODhhNy00NGE2LWFiZmUtYmU0ZmYwMTM0ZmY0" # str | The token used to redirect the buyer for approval of a transaction. This token does not represent anything to the consumer and no value should be derived from it except for internal use.

    # example passing only required values which don't have defaults set
    try:
        # Redirect buyer to service
        api_instance.redirect_transaction_approval(transaction_approval_token)
    except api.openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->redirect_transaction_approval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_approval_token** | **str**| The token used to redirect the buyer for approval of a transaction. This token does not represent anything to the consumer and no value should be derived from it except for internal use. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect the buyer to approve this transaction. |  * location - The URL to redirect the browser to. This is the approval URL for an alternative payment method like GoCardless. <br>  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_transaction**
> Transaction refund_transaction(transaction_id)

Refund or void transactions

Refunds or voids transaction. If this transaction was already captured, it will issue a refund. If the transaction was not yet captured the authorization will instead be voided.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import api.openapi_client
from gr4vy_api.openapi_client.api import transactions_api
from gr4vy_api.openapi_client.model.transaction_refund_request import TransactionRefundRequest
from gr4vy_api.openapi_client.model.transaction import Transaction
from gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = api.openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = api.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with api.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_id = "fe26475d-ec3e-4884-9553-f7356683f7f9" # str | The ID for the transaction to get the information for.
    transaction_refund_request = TransactionRefundRequest(
        amount=1299,
    ) # TransactionRefundRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Refund or void transactions
        api_response = api_instance.refund_transaction(transaction_id)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->refund_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Refund or void transactions
        api_response = api_instance.refund_transaction(transaction_id, transaction_refund_request=transaction_refund_request)
        pprint(api_response)
    except api.openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->refund_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The ID for the transaction to get the information for. |
 **transaction_refund_request** | [**TransactionRefundRequest**](TransactionRefundRequest.md)|  | [optional]

### Return type

[**Transaction**](Transaction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns cancelled transaction. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found or has not yet been created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

