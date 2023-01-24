# ApiLog

A log of an error that happened in the API call.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;api-log&#x60;. | [optional]  if omitted the server will use the default value of "api-log"
**id** | **str** | The ID of the API log entry. | [optional] 
**request_method** | **str** | The http request method that generated the log entry. | [optional] 
**request_url** | **str** | The http request URL which trigged the error log. | [optional] 
**request_received_at** | **datetime** | The date and time that the request was received. | [optional] 
**response_status_code** | **float** | The http request status code. | [optional] 
**response_body** | [**ApiLogResponseBody**](ApiLogResponseBody.md) |  | [optional] 
**response_sent_at** | **datetime** | date-time of when the response was sent. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


