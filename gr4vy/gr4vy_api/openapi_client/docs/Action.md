# Action

An action taken for a transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource. Is always &#x60;action&#x60;. | [optional]  if omitted the server will use the default value of "action"
**id** | **str** | The identifier for the action. | [optional] 
**flow** | **str** | The name of the Flow. | [optional] 
**rule_id** | **str** | The unique ID of the rule triggered. | [optional] 
**created_at** | **datetime** | The date and time when this action was created. | [optional] 
**outcome** | [**Undefined**](Undefined.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


