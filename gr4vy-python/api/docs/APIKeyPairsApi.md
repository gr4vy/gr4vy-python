# openapi_client.APIKeyPairsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key_pair**](APIKeyPairsApi.md#create_api_key_pair) | **POST** /api-key-pairs | Create an API key-pair
[**delete_api_key_pair**](APIKeyPairsApi.md#delete_api_key_pair) | **DELETE** /api-key-pairs/{api_key_pair_id} | Delete an API key-pair
[**list_api_key_pairs**](APIKeyPairsApi.md#list_api_key_pairs) | **GET** /api-key-pairs | List API key-pairs


# **create_api_key_pair**
> APIKeyPair create_api_key_pair()

Create an API key-pair

Creates a new API key-pair.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import api_key_pairs_api
from openapi_client.model.api_key_pair import APIKeyPair
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
    api_instance = api_key_pairs_api.APIKeyPairsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create an API key-pair
        api_response = api_instance.create_api_key_pair()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling APIKeyPairsApi->create_api_key_pair: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**APIKeyPair**](APIKeyPair.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns a newly created key pair. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key_pair**
> delete_api_key_pair(api_key_pair_id)

Delete an API key-pair

Deletes an API key-pair.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import api_key_pairs_api
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
    api_instance = api_key_pairs_api.APIKeyPairsApi(api_client)
    api_key_pair_id = "gg9ILy" # str | The ID for the API key pair.

    # example passing only required values which don't have defaults set
    try:
        # Delete an API key-pair
        api_instance.delete_api_key_pair(api_key_pair_id)
    except openapi_client.ApiException as e:
        print("Exception when calling APIKeyPairsApi->delete_api_key_pair: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_pair_id** | **str**| The ID for the API key pair. |

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

# **list_api_key_pairs**
> APIKeyPairs list_api_key_pairs()

List API key-pairs

Returns a list of active API key-pairs.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import api_key_pairs_api
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from openapi_client.model.api_key_pairs import APIKeyPairs
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
    api_instance = api_key_pairs_api.APIKeyPairsApi(api_client)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List API key-pairs
        api_response = api_instance.list_api_key_pairs(limit=limit, cursor=cursor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling APIKeyPairsApi->list_api_key_pairs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]

### Return type

[**APIKeyPairs**](APIKeyPairs.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of active key pairs. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

