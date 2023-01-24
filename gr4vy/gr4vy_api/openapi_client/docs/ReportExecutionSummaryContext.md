# ReportExecutionSummaryContext

Contains the context values used to compute the value of date-time placeholders such as `month_start` and `month_end` if present in the report's specification. Date-time placeholders are dynamic timestamps that change with every report execution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_timestamp** | **datetime** | The date and time used by the system as a reference point to compute date-time placeholders. | [optional] 
**reference_timezone** | **str** | The time zone used to compute date-time placeholders. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


