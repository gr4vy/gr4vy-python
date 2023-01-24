# CheckoutSessionRequest

Details for a Checkout Session payment method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Checkout Session. | 
**method** | **str** | &#x60;checkout-session&#x60;. | defaults to "checkout-session"
**external_identifier** | **str, none_type** | An external identifier that can be used to match the card against your own records. | [optional] 
**buyer_id** | **str** | The ID of the buyer to associate this payment method to. If this field is provided then the &#x60;buyer_external_identifier&#x60; field needs to be unset. | [optional] 
**buyer_external_identifier** | **str** | The &#x60;external_identifier&#x60; of the buyer to associate this payment method to. If this field is provided then the &#x60;buyer_id&#x60; field needs to be unset. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


