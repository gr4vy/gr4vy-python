# openapi_client.PaymentServiceDefinitionsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_service_definition**](PaymentServiceDefinitionsApi.md#get_payment_service_definition) | **GET** /payment-service-definitions/{payment_service_definition_id} | Get payment service definition
[**list_payment_service_definitions**](PaymentServiceDefinitionsApi.md#list_payment_service_definitions) | **GET** /payment-service-definitions | List payment service definitions


# **get_payment_service_definition**
> PaymentServiceDefinition get_payment_service_definition(payment_service_definition_id)

Get payment service definition

Gets the definition for a payment service.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_service_definitions_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from openapi_client.model.payment_service_definition import PaymentServiceDefinition
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
    api_instance = payment_service_definitions_api.PaymentServiceDefinitionsApi(api_client)
    payment_service_definition_id = "stripe-card" # str | The unique ID of the payment service definition.

    # example passing only required values which don't have defaults set
    try:
        # Get payment service definition
        api_response = api_instance.get_payment_service_definition(payment_service_definition_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentServiceDefinitionsApi->get_payment_service_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service_definition_id** | **str**| The unique ID of the payment service definition. |

### Return type

[**PaymentServiceDefinition**](PaymentServiceDefinition.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a payment service definition. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_service_definitions**
> PaymentServiceDefinitions list_payment_service_definitions()

List payment service definitions

Returns a list of all available payment service definitions.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_service_definitions_api
from openapi_client.model.payment_service_definitions import PaymentServiceDefinitions
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
    api_instance = payment_service_definitions_api.PaymentServiceDefinitionsApi(api_client)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List payment service definitions
        api_response = api_instance.list_payment_service_definitions(limit=limit, cursor=cursor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentServiceDefinitionsApi->list_payment_service_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]

### Return type

[**PaymentServiceDefinitions**](PaymentServiceDefinitions.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of payment service definitions. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

