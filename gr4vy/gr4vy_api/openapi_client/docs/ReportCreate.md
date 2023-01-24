# ReportCreate

A request to create a report.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the report. | 
**spec** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**description** | **str, none_type** | The description of the report. | [optional] 
**schedule** | **str** | Specifies the schedule of the report.  If this is a one-off report, set this value to &#x60;once&#x60;.  If this is a recurring report, this value should be set to the frequency by which the report will be executed. For example, a &#x60;monthly&#x60; schedule means that the report will be periodically executed at the start of each month.  Note that a &#x60;weekly&#x60; schedule means that the report will be executed at the start of every Monday. | [optional]  if omitted the server will use the default value of "once"
**schedule_enabled** | **bool, none_type** | Indicates whether the report&#39;s scheduling is enabled. This value can only be set to &#x60;true&#x60; if this is a recurring report.  If this value is set to &#x60;true&#x60;, the report will be executed at the &#x60;next_execution_at&#x60; date and time.  If this is a recurring report and this value is set to &#x60;false&#x60;, executions of the report will not occur until this value is set to &#x60;true&#x60;.  If this value is not provided, &#x60;schedule_enabled&#x60; will automatically be set to &#x60;false&#x60; if &#x60;schedule&#x60; is &#x60;once&#x60; and set to &#x60;true&#x60; otherwise. | [optional] 
**schedule_timezone** | **str** | The time zone in which the report&#39;s executions will be scheduled. This value is used to compute the report&#39;s &#x60;next_execution_at&#x60; value and is only relevant when this is a recurring report. This time zone is also used to calculate the timestamp range for reports that use date-time placeholders. Date-time placeholders are dynamic timestamps that change with every report execution.  This value must be set to the time zone&#39;s name as presented in the IANA time zone database. For example, to schedule reports in the time zone of New York, set this value to &#x60;America/New_York&#x60;. | [optional]  if omitted the server will use the default value of "Etc/UTC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


