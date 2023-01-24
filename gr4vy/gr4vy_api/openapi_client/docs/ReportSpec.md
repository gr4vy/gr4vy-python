# ReportSpec

The specification of a report.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Parameters used to configure the report. Acceptable values for this property depend on the value specified for &#x60;model&#x60;. | 
**model** | **str** | The model (dataset) that the data used for the report is retrieved from. | defaults to "transactions"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


