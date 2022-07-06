# FlowPaymentOptionOutcome

Outcome for checkout flow/select payment options action. Each option is a Gr4vy payment option object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource. Is always &#x60;action&#x60;. | [optional]  if omitted the server will use the default value of "action"
**id** | **str** | Payment option identifier. | [optional] 
**label** | **str** | Verbose payment option name. | [optional] 
**active** | **bool** | The status of the payment option, true if at least one underlying connection is active, otherwise false. | [optional] 
**group** | **str, none_type** | Optional group label for a given payment option, e.g. &#x60;Bank&#x60;. | [optional] 
**icon_url** | **str** | Payment option icon URL. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


