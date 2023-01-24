# ReportExecution

A report execution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The report associated with this report execution. | [optional] 
**type** | **str** | The type of this resource. Is always &#x60;report-execution&#x60;. | [optional]  if omitted the server will use the default value of "report-execution"
**id** | **str** | The unique identifier for this report execution. | [optional] 
**created_at** | **datetime** | The date and time this report execution was created in our system. | [optional] 
**updated_at** | **datetime** | The date and time this report execution was last updated. | [optional] 
**status** | **str** | The status of this report execution. | [optional] 
**context** | [**ReportExecutionSummaryContext**](ReportExecutionSummaryContext.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


