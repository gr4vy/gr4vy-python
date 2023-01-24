# openapi_client.ReportsApi

All URIs are relative to *https://api.plantly.gr4vy.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_report**](ReportsApi.md#add_report) | **POST** /reports | New report
[**generate_download_url**](ReportsApi.md#generate_download_url) | **POST** /reports/{report_id}/executions/{report_execution_id}/url | Generate the download URL of a report execution result
[**get_report**](ReportsApi.md#get_report) | **GET** /reports/{report_id} | Get report
[**get_report_execution**](ReportsApi.md#get_report_execution) | **GET** /report-executions/{report_execution_id} | Get report execution
[**list_all_report_executions**](ReportsApi.md#list_all_report_executions) | **GET** /report-executions | List all report executions
[**list_report_executions**](ReportsApi.md#list_report_executions) | **GET** /reports/{report_id}/executions | List executions for a report
[**list_reports**](ReportsApi.md#list_reports) | **GET** /reports | List reports
[**update_report**](ReportsApi.md#update_report) | **PUT** /reports/{report_id} | Update report


# **add_report**
> Report add_report()

New report

Adds a report.  Documentation about reports models and how to write a valid specification can be found in [Reporting docs](/reporting/introduction). 

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import reports_api
from openapi_client.model.report import Report
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.report_create import ReportCreate
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
    api_instance = reports_api.ReportsApi(api_client)
    report_create = ReportCreate(
        name="Failed Authorizations 042022",
        description="Transactions that failed to authorize in April 2022",
        schedule="monthly",
        schedule_enabled=True,
        schedule_timezone="Europe/London",
        spec=None,
    ) # ReportCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # New report
        api_response = api_instance.add_report(report_create=report_create)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReportsApi->add_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_create** | [**ReportCreate**](ReportCreate.md)|  | [optional]

### Return type

[**Report**](Report.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the report that was added. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_download_url**
> ReportExecutionUrl generate_download_url(report_id, report_execution_id)

Generate the download URL of a report execution result

Generates a temporary signed URL to download the result of a report execution.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import reports_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.report_execution_url import ReportExecutionUrl
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
    api_instance = reports_api.ReportsApi(api_client)
    report_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a report.
    report_execution_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a report execution.

    # example passing only required values which don't have defaults set
    try:
        # Generate the download URL of a report execution result
        api_response = api_instance.generate_download_url(report_id, report_execution_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReportsApi->generate_download_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The unique ID for a report. |
 **report_execution_id** | **str**| The unique ID for a report execution. |

### Return type

[**ReportExecutionUrl**](ReportExecutionUrl.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the signed download URL of a report execution result and its expiration date and time. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> Report get_report(report_id)

Get report

Retrieves the details of a single report.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import reports_api
from openapi_client.model.report import Report
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
    api_instance = reports_api.ReportsApi(api_client)
    report_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a report.

    # example passing only required values which don't have defaults set
    try:
        # Get report
        api_response = api_instance.get_report(report_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReportsApi->get_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The unique ID for a report. |

### Return type

[**Report**](Report.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a report. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_execution**
> ReportExecution get_report_execution(report_execution_id)

Get report execution

Retrieves the details of a single report execution.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import reports_api
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.report_execution import ReportExecution
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
    api_instance = reports_api.ReportsApi(api_client)
    report_execution_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a report execution.

    # example passing only required values which don't have defaults set
    try:
        # Get report execution
        api_response = api_instance.get_report_execution(report_execution_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReportsApi->get_report_execution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_execution_id** | **str**| The unique ID for a report execution. |

### Return type

[**ReportExecution**](ReportExecution.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a report execution. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_report_executions**
> ReportExecutions list_all_report_executions()

List all report executions

Returns a list of executions belonging to any report.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import reports_api
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from openapi_client.model.report_executions import ReportExecutions
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
    api_instance = reports_api.ReportsApi(api_client)
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    created_at_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filters the results to report executions created after this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`. (optional)
    created_at_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filters the results to report executions created before this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`. (optional)
    report_name = "Failed+Authorizations+042022" # str | Filters for executions of reports that have a matching `name` value. This filter is case-insensitive.  Ensure that when necessary, the value you pass for this filter is URL encoded. (optional)
    status = ["succeeded","failed"] # [str] | Filters for report executions that have a matching `status` value.  This filter accepts multiple values. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all report executions
        api_response = api_instance.list_all_report_executions(cursor=cursor, limit=limit, created_at_gte=created_at_gte, created_at_lte=created_at_lte, report_name=report_name, status=status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReportsApi->list_all_report_executions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **created_at_gte** | **datetime**| Filters the results to report executions created after this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. &#x60;2022-01-01T12:00:00+08:00&#x60; must be encoded as &#x60;2022-01-01T12%3A00%3A00%2B08%3A00&#x60;. | [optional]
 **created_at_lte** | **datetime**| Filters the results to report executions created before this ISO date-time string. The time zone must be included.  Ensure that the date-time string is URL encoded, e.g. &#x60;2022-01-01T12:00:00+08:00&#x60; must be encoded as &#x60;2022-01-01T12%3A00%3A00%2B08%3A00&#x60;. | [optional]
 **report_name** | **str**| Filters for executions of reports that have a matching &#x60;name&#x60; value. This filter is case-insensitive.  Ensure that when necessary, the value you pass for this filter is URL encoded. | [optional]
 **status** | **[str]**| Filters for report executions that have a matching &#x60;status&#x60; value.  This filter accepts multiple values. | [optional]

### Return type

[**ReportExecutions**](ReportExecutions.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of report executions. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_report_executions**
> ReportExecutions list_report_executions(report_id)

List executions for a report

Returns a list of executions for a report.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import reports_api
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from openapi_client.model.report_executions import ReportExecutions
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
    api_instance = reports_api.ReportsApi(api_client)
    report_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a report.
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    try:
        # List executions for a report
        api_response = api_instance.list_report_executions(report_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReportsApi->list_report_executions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List executions for a report
        api_response = api_instance.list_report_executions(report_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReportsApi->list_report_executions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The unique ID for a report. |
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20

### Return type

[**ReportExecutions**](ReportExecutions.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of executions for a report. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reports**
> Reports list_reports()

List reports

Returns a list of reports.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import reports_api
from openapi_client.model.reports import Reports
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
    api_instance = reports_api.ReportsApi(api_client)
    cursor = "ZXhhbXBsZTE" # str | A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list. (optional)
    limit = 1 # int | Defines the maximum number of items to return for this request. (optional) if omitted the server will use the default value of 20
    name = "Failed+Authorizations+042022" # str | Filters for reports that have a matching `name` value. This filter is case-insensitive.  Ensure that when necessary, the value you pass for this filter is URL encoded. (optional)
    schedule = ["once","monthly"] # [str] | Filters for reports that have matching `schedule` values. (optional)
    schedule_enabled = True # bool | Filters for reports that have a matching `schedule_enabled` value. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List reports
        api_response = api_instance.list_reports(cursor=cursor, limit=limit, name=name, schedule=schedule, schedule_enabled=schedule_enabled)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReportsApi->list_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the &#x60;next_cursor&#x60; field. Similarly the &#x60;previous_cursor&#x60; can be used to reverse backwards in the list. | [optional]
 **limit** | **int**| Defines the maximum number of items to return for this request. | [optional] if omitted the server will use the default value of 20
 **name** | **str**| Filters for reports that have a matching &#x60;name&#x60; value. This filter is case-insensitive.  Ensure that when necessary, the value you pass for this filter is URL encoded. | [optional]
 **schedule** | **[str]**| Filters for reports that have matching &#x60;schedule&#x60; values. | [optional]
 **schedule_enabled** | **bool**| Filters for reports that have a matching &#x60;schedule_enabled&#x60; value. | [optional]

### Return type

[**Reports**](Reports.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of reports. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report**
> Report update_report(report_id)

Update report

Updates a report.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import openapi_client
from openapi_client.api import reports_api
from openapi_client.model.report import Report
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.error_generic import ErrorGeneric
from openapi_client.model.report_update import ReportUpdate
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
    api_instance = reports_api.ReportsApi(api_client)
    report_id = "8724fd24-5489-4a5d-90fd-0604df7d3b83" # str | The unique ID for a report.
    report_update = ReportUpdate(
        name="Failed Authorizations 042022",
        description="Transactions that failed to authorize in April 2022",
        schedule_enabled=True,
    ) # ReportUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update report
        api_response = api_instance.update_report(report_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReportsApi->update_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update report
        api_response = api_instance.update_report(report_id, report_update=report_update)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReportsApi->update_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The unique ID for a report. |
 **report_update** | [**ReportUpdate**](ReportUpdate.md)|  | [optional]

### Return type

[**Report**](Report.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated report. |  -  |
**400** | Returns an error if the request was badly formatted or missing required fields. |  -  |
**401** | Returns an error if no valid authentication was provided. |  -  |
**404** | Returns an error if the resource can not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

