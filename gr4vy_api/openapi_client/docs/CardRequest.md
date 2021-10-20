# CardRequest

Card details to use in a transaction or to register a new payment method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | The 15-16 digit number for this card as it can be found on the front of the card. | 
**expiration_date** | **str** | The expiration date of the card, formatted &#x60;MM/YY&#x60;. | 
**security_code** | **str** | The 3 or 4 digit security code often found on the card. This often referred to as the CVV or CVD. | 
**method** | **str** | &#x60;card&#x60;. | defaults to "card"
**external_identifier** | **str, none_type** | An external identifier that can be used to match the card against your own records. | [optional] 
**buyer_id** | **str** | The ID of the buyer to associate this payment method to. If this field is provided then the &#x60;buyer_external_identifier&#x60; field needs to be unset. | [optional] 
**buyer_external_identifier** | **str** | The &#x60;external_identifier&#x60; of the buyer to associate this payment method to. If this field is provided then the &#x60;buyer_id&#x60; field needs to be unset. | [optional] 
**environment** | **str** | Defines the environment to store this card for. Setting this to anything other than &#x60;production&#x60; will force Gr4vy to use the payment services configured for that environment. | [optional] 
**redirect_url** | **str** | The redirect URL to redirect a buyer after a 3D Secure flow has been completed. This will be appended with both a transaction ID and status (e.g. &#x60;https://example.com/callback? gr4vy_transaction_id&#x3D;123&amp;gr4vy_transaction_status&#x3D;capture_succeeded&#x60;). This is required if the transaction request body does not include &#x60;three_d_secure_data&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


