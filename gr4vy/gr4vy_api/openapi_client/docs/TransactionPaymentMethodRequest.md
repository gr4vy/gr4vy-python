# TransactionPaymentMethodRequest

Payment method details to use in a transaction or to register a new payment method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **object** |  | 
**number** | **str** | The 15-16 digit number for this credit card as it can be found on the front of the card.  If a card has been stored with us previously, this number will represent the unique tokenized card ID provided via our API. | [optional] 
**expiration_date** | **str** | The expiration date of the card, formatted &#x60;MM/YY&#x60;. If a card has been previously stored with us this value is optional.  If the &#x60;number&#x60; of this card represents a tokenized card, then this value is ignored. | [optional] 
**security_code** | **str** | The 3 or 4 digit security code often found on the card. This often referred to as the CVV or CVD.  If the &#x60;number&#x60; of this card represents a tokenized card, then this value is ignored. | [optional] 
**external_identifier** | **str, none_type** | An external identifier that can be used to match the card against your own records. | [optional] 
**buyer_id** | **str** | The ID of the buyer to associate this payment method to. If this field is provided then the &#x60;buyer_external_identifier&#x60; field needs to be unset. | [optional] 
**buyer_external_identifier** | **str** | The &#x60;external_identifier&#x60; of the buyer to associate this payment method to. If this field is provided then the &#x60;buyer_id&#x60; field needs to be unset. | [optional] 
**redirect_url** | **str** | The redirect URL to redirect a buyer to after they have authorized their transaction or payment method. This only applies to payment methods that require buyer approval. | [optional] 
**id** | **str** | An identifier for a previously tokenized payment method. This id can represent any type of payment method. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


