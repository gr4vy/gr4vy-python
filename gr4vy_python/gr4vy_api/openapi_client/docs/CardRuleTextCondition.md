# CardRuleTextCondition

Part of a rule that matches text fields. It defines the condition under which this rule applies.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The transaction field to filter by. | 
**operator** | **str** | The comparison to make to &#x60;value&#x60; property. | 
**value** | **[str]** | The values to compare the &#x60;key&#x60; to. | 
**match** | **str** | &#x60;text&#x60;. | defaults to "text"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


