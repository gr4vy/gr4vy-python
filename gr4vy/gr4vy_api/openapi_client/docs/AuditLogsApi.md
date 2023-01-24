# openapi_client.AuditLogsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_audit_logs**](AuditLogsApi.md#list_audit_logs) | **GET** /audit-logs | List Audit Logs


# **list_audit_logs**
> AuditLogs list_audit_logs()

List Audit Logs

Returns a list of audit logs.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import audit_logs_api
from openapi_client.model.audit_logs import AuditLogs
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
    api_instance = audit_logs_api.AuditLogsApi(api_client)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)
    user_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | Filters the results to only the items for which the `user` has an `id` that matches this value. (optional)
    action = "created" # str | Filters the results to only the items for which the `audit-log` has an `action` that matches this value. (optional)
    resource_type = "buyer" # str | Filters the results to only the items for which the `audit-log` has a `resource` that matches this type value. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Audit Logs
        api_response = api_instance.list_audit_logs(limit=limit, cursor=cursor, user_id=user_id, action=action, resource_type=resource_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuditLogsApi->list_audit_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]
 **user_id** | **str**| Filters the results to only the items for which the &#x60;user&#x60; has an &#x60;id&#x60; that matches this value. | [optional]
 **action** | **str**| Filters the results to only the items for which the &#x60;audit-log&#x60; has an &#x60;action&#x60; that matches this value. | [optional]
 **resource_type** | **str**| Filters the results to only the items for which the &#x60;audit-log&#x60; has a &#x60;resource&#x60; that matches this type value. | [optional]

### Return type

[**AuditLogs**](AuditLogs.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of audit logs. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

