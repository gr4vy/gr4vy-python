# PaymentServiceDefinitions

A list of available payment services definitions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[PaymentServiceDefinition]**](PaymentServiceDefinition.md) |  | [optional] 
**limit** | **int** | The limit applied to request. This represents the number of items that are at maximum returned by this request. | [optional]  if omitted the server will use the default value of 20
**next_cursor** | **str, none_type** | The cursor that represents the next page of results. Use the &#x60;cursor&#x60; query parameter to fetch this page of items. | [optional] 
**previous_cursor** | **str, none_type** | The cursor that represents the next page of results. Use the &#x60;cursor&#x60; query parameter to fetch this page of items. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


