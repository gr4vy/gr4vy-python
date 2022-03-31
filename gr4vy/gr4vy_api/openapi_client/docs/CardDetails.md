# CardDetails

Details about a card.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;card-detail&#x60;. | [optional]  if omitted the server will use the default value of "card-detail"
**id** | **str** | The 6-8 digit BIN of the card. | [optional] 
**card_type** | **str** | The type of card. | [optional] 
**scheme** | **str** | The scheme/brand of the card. | [optional] 
**country** | **str** | The 2-letter ISO code of the issuing country of the card. | [optional] 
**required_fields** | **[str]** | A list of fields that are required to process a transaction for this card. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


