# PaymentMethodSnapshot

Snapshot of a payment method, as used when embedded inside other resources.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;payment-method&#x60;. | [optional]  if omitted the server will use the default value of "payment-method"
**id** | **str, none_type** | The unique ID of the payment method. | [optional] 
**method** | **object** |  | [optional] 
**external_identifier** | **str, none_type** | An external identifier that can be used to match the payment method against your own records. | [optional] 
**label** | **str** | A label for the payment method. This can be the last 4 digits for a card, or the email address for an alternative payment method. | [optional] 
**scheme** | **str, none_type** | An additional label used to differentiate different sub-types of a payment method. Most notably this can include the type of card used in a transaction. | [optional] 
**expiration_date** | **str, none_type** | The expiration date for this payment method. This is mostly used by cards where the card might have an expiration date. | [optional] 
**approval_url** | **str, none_type** | The optional URL that the buyer needs to be redirected to to further authorize their payment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


