# BuyerSnapshot

Snapshot of a buyer, as used when embedded inside other resources.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource. Is always &#x60;buyer&#x60;. | [optional]  if omitted the server will use the default value of "buyer"
**id** | **str** | The unique Gr4vy ID for this buyer. | [optional] 
**external_identifier** | **str, none_type** | An external identifier that can be used to match the buyer against your own records. | [optional] 
**display_name** | **str, none_type** | A unique name for this buyer which is used in the Gr4vy admin panel to give a buyer a human readable name. | [optional] 
**billing_details** | **bool, date, datetime, dict, float, int, list, str, none_type** | The billing details associated with the buyer, which include the address and tax ID. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


