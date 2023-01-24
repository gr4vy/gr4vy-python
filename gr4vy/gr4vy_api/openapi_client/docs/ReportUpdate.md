# ReportUpdate

Request body to update a report.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the report. | [optional] 
**description** | **str, none_type** | The description of the report. | [optional] 
**schedule_enabled** | **bool** | Indicates whether the report&#39;s scheduling is enabled. This value can only be set to &#x60;true&#x60; if this is a recurring report.  When this value is set to &#x60;true&#x60;, the report will be executed at the &#x60;next_execution_at&#x60; date and time.  When this value is set to &#x60;false&#x60;, future executions of the report are paused until this value is set to &#x60;true&#x60; again.  If scheduling is enabled after being disabled, then the &#x60;next_execution_at&#x60; value is updated if and only if its current value is a past date-time. The &#x60;next_execution_at&#x60; value is then set to the next closest date-time in the future depending on the values of &#x60;schedule&#x60; and &#x60;schedule_timezone&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


