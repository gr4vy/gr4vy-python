# openapi_client.PaymentMethodTokensApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_payment_method_tokens**](PaymentMethodTokensApi.md#list_payment_method_tokens) | **GET** /payment-methods/{payment_method_id}/tokens | List payment method tokens


# **list_payment_method_tokens**
> PaymentMethodTokens list_payment_method_tokens(payment_method_id)

List payment method tokens

Returns a list of PSP tokens for a given payment method.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_method_tokens_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.payment_method_tokens import PaymentMethodTokens
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
    api_instance = payment_method_tokens_api.PaymentMethodTokensApi(api_client)
    payment_method_id = "46973e9d-88a7-44a6-abfe-be4ff0134ff4" # str | The ID of the payment method.

    # example passing only required values which don't have defaults set
    try:
        # List payment method tokens
        api_response = api_instance.list_payment_method_tokens(payment_method_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodTokensApi->list_payment_method_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| The ID of the payment method. |

### Return type

[**PaymentMethodTokens**](PaymentMethodTokens.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of payment method tokens. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

