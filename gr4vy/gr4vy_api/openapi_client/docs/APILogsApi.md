# openapi_client.APILogsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_api_logs**](APILogsApi.md#list_api_logs) | **GET** /api-logs | List API error Logs


# **list_api_logs**
> ApiLogs list_api_logs()

List API error Logs

Returns a list of API 4XX and 5XX logs.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import api_logs_api
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from openapi_client.model.api_logs import ApiLogs
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
    api_instance = api_logs_api.APILogsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List API error Logs
        api_response = api_instance.list_api_logs()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling APILogsApi->list_api_logs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiLogs**](ApiLogs.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of API logs. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

