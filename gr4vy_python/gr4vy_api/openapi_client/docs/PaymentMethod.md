# PaymentMethod

A generic payment method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;payment-method&#x60;. | [optional]  if omitted the server will use the default value of "payment-method"
**id** | **str** | The unique ID of the payment method. | [optional] 
**status** | **str** | The state of the payment method.  - &#x60;processing&#x60; - The payment method is still being stored. - &#x60;buyer_approval_required&#x60; - Storing the payment method requires   the buyer to provide approval. Follow the &#x60;approval_url&#x60; for next steps. - &#x60;succeeded&#x60; - The payment method is approved and stored with all   relevant payment services. - &#x60;failed&#x60; - Storing the payment method did not succeed. | [optional] 
**method** | **object** |  | [optional] 
**mode** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time when this payment method was first created in our system. | [optional] 
**updated_at** | **datetime** | The date and time when this payment method was last updated in our system. | [optional] 
**external_identifier** | **str, none_type** | An external identifier that can be used to match the payment method against your own records. | [optional] 
**buyer** | **object** |  | [optional] 
**label** | **str, none_type** | A label for the card or the account. For a &#x60;paypal&#x60; payment method this is the user&#39;s email address. For a card it is the last 4 digits of the card. | [optional] 
**scheme** | **str, none_type** | The scheme of the card. Only applies to card payments. | [optional] 
**expiration_date** | **str, none_type** | The expiration date for the payment method. | [optional] 
**approval_url** | **str, none_type** | The optional URL that the buyer needs to be redirected to to further authorize their payment. | [optional] 
**environment** | **str, none_type** | The environment this payment method has been stored for. This will be null of the payment method was not stored. | [optional]  if omitted the server will use the default value of "production"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


