# CardDetails

Details about a card.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;card-detail&#x60;. | [optional]  if omitted the server will use the default value of "card-detail"
**id** | **str** | The 8 digit BIN of the card. When looking up card details using a &#x60;payment_method_id&#x60; this value will be &#x60;null&#x60;. | [optional] 
**card_type** | **str** | The type of card. | [optional] 
**scheme** | **str** | The scheme/brand of the card. | [optional] 
**scheme_icon_url** | **str** | An icon to display for the card scheme. | [optional] 
**country** | **str** | The 2-letter ISO code of the issuing country of the card. | [optional] 
**required_fields** | [**RequiredFields**](RequiredFields.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


