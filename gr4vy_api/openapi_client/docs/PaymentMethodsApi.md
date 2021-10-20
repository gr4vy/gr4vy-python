# openapi_client.PaymentMethodsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_payment_method**](PaymentMethodsApi.md#approve_payment_method) | **GET** /payment-methods/{payment_method_id}/approve/{payment_service_id} | Buyer approval callback
[**delete_payment_method**](PaymentMethodsApi.md#delete_payment_method) | **DELETE** /payment-methods/{payment_method_id} | Delete payment method
[**get_payment_method**](PaymentMethodsApi.md#get_payment_method) | **GET** /payment-methods/{payment_method_id} | Get stored payment method
[**list_buyer_payment_methods**](PaymentMethodsApi.md#list_buyer_payment_methods) | **GET** /buyers/payment-methods | List stored payment methods for a buyer
[**list_payment_methods**](PaymentMethodsApi.md#list_payment_methods) | **GET** /payment-methods | List payment methods
[**redirect_payment_method_approval**](PaymentMethodsApi.md#redirect_payment_method_approval) | **GET** /payment-methods/approvals/{payment_method_approval_token} | Redirect buyer to service
[**store_payment_method**](PaymentMethodsApi.md#store_payment_method) | **POST** /payment-methods | New payment method


# **approve_payment_method**
> approve_payment_method(payment_method_id, payment_service_id)

Buyer approval callback

Internal API used as a redirect endpoint for payment methods that require buyer authorization.  For example, when a buyer tries to add a GoCardless payment method, the buyer needs to be sent to them, after which they are sent back to this endpoint upon completion.  This API applies any required updates for the payment method based on its query parameters and then redirects the browser back to the `redirect_url` specified when the payment method was first created.

### Example

```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.error404_not_found import Error404NotFound
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    payment_method_id = "46973e9d-88a7-44a6-abfe-be4ff0134ff4" # str | The ID of the payment method.
    payment_service_id = "46973e9d-88a7-44a6-abfe-be4ff0134ff4" # str | The ID of the payment service.

    # example passing only required values which don't have defaults set
    try:
        # Buyer approval callback
        api_instance.approve_payment_method(payment_method_id, payment_service_id)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->approve_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| The ID of the payment method. |
 **payment_service_id** | **str**| The ID of the payment service. |

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
**302** | Redirects the browser back to the &#x60;redirect_url&#x60; specified when the payment method was first created. It appends the payment method&#39;s ID and status. |  * location - The URL to redirect the browser to. This is the &#x60;redirect_url&#x60; specified when the payment method was first created with some additional query parameters appended.  * &#x60;payment_method_id&#x60; - The ID of the payment method. * &#x60;payment_method_status&#x60; - The current value of the   &#x60;status&#x60;  field of the payment method. <br>  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method**
> delete_payment_method(payment_method_id)

Delete payment method

Removes a stored payment method.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    payment_method_id = "46973e9d-88a7-44a6-abfe-be4ff0134ff4" # str | The ID of the payment method.

    # example passing only required values which don't have defaults set
    try:
        # Delete payment method
        api_instance.delete_payment_method(payment_method_id)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->delete_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| The ID of the payment method. |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns an empty response. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method**
> PaymentMethod get_payment_method(payment_method_id)

Get stored payment method

Gets the details for a stored payment method.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.payment_method import PaymentMethod
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    payment_method_id = "46973e9d-88a7-44a6-abfe-be4ff0134ff4" # str | The ID of the payment method.

    # example passing only required values which don't have defaults set
    try:
        # Get stored payment method
        api_response = api_instance.get_payment_method(payment_method_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->get_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| The ID of the payment method. |

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a payment method. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_payment_methods**
> PaymentMethodsTokenized list_buyer_payment_methods()

List stored payment methods for a buyer

Returns a list of stored (tokenized) payment methods for a buyer in a short tokenized format. Only payment methods that are compatible with at least one active payment service in that region are shown.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.payment_methods_tokenized import PaymentMethodsTokenized
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    buyer_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | Filters the results to only the items for which the `buyer` has an `id` that matches this value. (optional)
    buyer_external_identifier = "user-12345" # str | Filters the results to only the items for which the `buyer` has an `external_identifier` that matches this value. (optional)
    country = "US" # str | Filters the results to only the items which support this country code. A country is formatted as 2-letter ISO country code. (optional)
    currency = "USD" # str | Filters the results to only the items which support this currency code. A currency is formatted as 3-letter ISO currency code. (optional)
    environment = "staging" # str | Filters the results to only the items available in this environment. (optional) if omitted the server will use the default value of "production"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List stored payment methods for a buyer
        api_response = api_instance.list_buyer_payment_methods(buyer_id=buyer_id, buyer_external_identifier=buyer_external_identifier, country=country, currency=currency, environment=environment)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->list_buyer_payment_methods: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| Filters the results to only the items for which the &#x60;buyer&#x60; has an &#x60;id&#x60; that matches this value. | [optional]
 **buyer_external_identifier** | **str**| Filters the results to only the items for which the &#x60;buyer&#x60; has an &#x60;external_identifier&#x60; that matches this value. | [optional]
 **country** | **str**| Filters the results to only the items which support this country code. A country is formatted as 2-letter ISO country code. | [optional]
 **currency** | **str**| Filters the results to only the items which support this currency code. A currency is formatted as 3-letter ISO currency code. | [optional]
 **environment** | **str**| Filters the results to only the items available in this environment. | [optional] if omitted the server will use the default value of "production"

### Return type

[**PaymentMethodsTokenized**](PaymentMethodsTokenized.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of available payment methods for a buyer, filtered by the given currency and country code. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_methods**
> PaymentMethods list_payment_methods()

List payment methods

Returns a list of stored (tokenized) payment methods.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.payment_methods import PaymentMethods
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    environment = "staging" # str | Filters the results to only the items available in this environment. (optional) if omitted the server will use the default value of "production"
    buyer_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | Filters the results to only the items for which the `buyer` has an `id` that matches this value. (optional)
    buyer_external_identifier = "user-12345" # str | Filters the results to only the items for which the `buyer` has an `external_identifier` that matches this value. (optional)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List payment methods
        api_response = api_instance.list_payment_methods(environment=environment, buyer_id=buyer_id, buyer_external_identifier=buyer_external_identifier, limit=limit, cursor=cursor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->list_payment_methods: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Filters the results to only the items available in this environment. | [optional] if omitted the server will use the default value of "production"
 **buyer_id** | **str**| Filters the results to only the items for which the &#x60;buyer&#x60; has an &#x60;id&#x60; that matches this value. | [optional]
 **buyer_external_identifier** | **str**| Filters the results to only the items for which the &#x60;buyer&#x60; has an &#x60;external_identifier&#x60; that matches this value. | [optional]
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]

### Return type

[**PaymentMethods**](PaymentMethods.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of payment methods. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redirect_payment_method_approval**
> redirect_payment_method_approval(payment_method_approval_token)

Redirect buyer to service

Redirect a buyer to an alternative payment provider to approve their payment method. This is mainly used with providers like GoCardless and Klarna to redirect a buyer to their sites.

### Example

```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.error404_not_found import Error404NotFound
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    payment_method_approval_token = "NDY5NzNlOWQtODhhNy00NGE2LWFiZmUtYmU0ZmYwMTM0ZmY0" # str | The token used to redirect the buyer for approval of the payment method setup. This token does not represent anything to the consumer and no value should be derived from it except for internal use.

    # example passing only required values which don't have defaults set
    try:
        # Redirect buyer to service
        api_instance.redirect_payment_method_approval(payment_method_approval_token)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->redirect_payment_method_approval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_approval_token** | **str**| The token used to redirect the buyer for approval of the payment method setup. This token does not represent anything to the consumer and no value should be derived from it except for internal use. |

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
**302** | Redirect the buyer to approve this payment method. |  * location - The URL to redirect the browser to. This is the approval URL for an alternative payment method like GoCardless. <br>  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_payment_method**
> PaymentMethod store_payment_method()

New payment method

Stores and tokenizes a new payment method.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_client.model.payment_method import PaymentMethod
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from pprint import pprint
# Defining the host is optional and defaults to https://api.plantly.gr4vy.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.plantly.gr4vy.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    unknown_base_type =  # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New payment method
        api_response = api_instance.store_payment_method(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->store_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the created payment method. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

