# openapi_client.PaymentMethodsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_payment_method**](PaymentMethodsApi.md#delete_payment_method) | **DELETE** /payment-methods/{payment_method_id} | Delete payment method
[**get_payment_method**](PaymentMethodsApi.md#get_payment_method) | **GET** /payment-methods/{payment_method_id} | Get stored payment method
[**list_buyer_payment_methods**](PaymentMethodsApi.md#list_buyer_payment_methods) | **GET** /buyers/payment-methods | List stored payment methods for a buyer
[**list_payment_methods**](PaymentMethodsApi.md#list_payment_methods) | **GET** /payment-methods | List payment methods
[**store_payment_method**](PaymentMethodsApi.md#store_payment_method) | **POST** /payment-methods | New payment method


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
from openapi_client.model.payment_method_request import PaymentMethodRequest
from openapi_client.model.error_generic import ErrorGeneric
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
    payment_method_request = PaymentMethodRequest(
        method=,
        number="4111111111111111",
        expiration_date="11/15",
        security_code="123",
        external_identifier="account-23423423",
        buyer_id="fe26475d-ec3e-4884-9553-f7356683f7f9",
        buyer_external_identifier="user-789123",
        redirect_url="https://example.com/callback",
        currency="USD",
        country="USD",
        environment="staging",
    ) # PaymentMethodRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New payment method
        api_response = api_instance.store_payment_method(payment_method_request=payment_method_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->store_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_request** | [**PaymentMethodRequest**](PaymentMethodRequest.md)|  | [optional]

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

