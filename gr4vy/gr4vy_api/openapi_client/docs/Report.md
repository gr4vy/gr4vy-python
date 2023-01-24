# Report

A report record.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date and time this report was created in our system. | [optional] 
**updated_at** | **datetime** | The date and time this report was last updated. | [optional] 
**next_execution_at** | **datetime, none_type** | The date and time this report will next be executed, provided that &#x60;schedule_enabled&#x60; is &#x60;true&#x60;. This value is null if this is a one-off report. | [optional] 
**description** | **str, none_type** | The description of this report. | [optional] 
**schedule** | **str** | Specifies the schedule of this report.  If this is a one-off report, this value is &#x60;once&#x60;.  If this is a recurring report, this value is set to the frequency by which the report will be executed. For example, a &#x60;monthly&#x60; schedule means that this report will be periodically executed at the start of each month.  Note that a &#x60;weekly&#x60; schedule means that the report is executed at the start of every Monday. | [optional] 
**schedule_enabled** | **bool** | Indicates whether this report&#39;s scheduling is enabled. This value can only be set to &#x60;true&#x60; if this is a recurring report.  When this value is set to &#x60;true&#x60;, this report will be executed at the &#x60;next_execution_at&#x60; date and time.  When this value is set to &#x60;false&#x60;, future executions of this report are paused until this value is set to &#x60;true&#x60; again. | [optional] 
**schedule_timezone** | **str** | The time zone in which the next execution will be scheduled. This value is used to calculate this report&#39;s &#x60;next_execution_at&#x60; value and is only relevant if this is a recurring report. This time zone is also used to calculate the timestamp range for reports that use date-time placeholders. Date-time placeholders are dynamic timestamps that change with every report execution. | [optional] 
**spec** | **bool, date, datetime, dict, float, int, list, str, none_type** | The specifications of this report. | [optional] 
**latest_execution** | **bool, date, datetime, dict, float, int, list, str, none_type** | Details of the latest execution of this report. | [optional] 
**type** | **str** | The type of this resource. Is always &#x60;report&#x60;. | [optional]  if omitted the server will use the default value of "report"
**id** | **str** | The unique identifier for this report. | [optional] 
**name** | **str** | The name of this report. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


