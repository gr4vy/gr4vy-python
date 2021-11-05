# TransactionRequest

A request to create a transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The monetary amount to create an authorization for, in the smallest currency unit for the given currency, for example &#x60;1299&#x60; cents to create an authorization for &#x60;$12.99&#x60;. | 
**currency** | **str** | A supported ISO-4217 currency code. | 
**payment_method** | [**TransactionPaymentMethodRequest**](TransactionPaymentMethodRequest.md) |  | 
**store** | **bool** | Whether or not to also try and store the payment method with us so that it can be used again for future use. This is only supported for payment methods that support this feature. | [optional]  if omitted the server will use the default value of False
**intent** | **str** | Defines the intent of this API call. This determines the desired initial state of the transaction.  * &#x60;authorize&#x60; - (Default) Optionally approves and then authorizes a transaction but does not capture the funds. * &#x60;capture&#x60; - Optionally approves and then authorizes and captures the funds of the transaction. | [optional]  if omitted the server will use the default value of "authorize"
**external_identifier** | **str, none_type** | An external identifier that can be used to match the transaction against your own records. | [optional] 
**environment** | **str** | Defines the environment to create this transaction in. Setting this to anything other than &#x60;production&#x60; will force Gr4vy to use the payment a service configured for that environment. | [optional] 
**three_d_secure_data** | [**ThreeDSecureDataV1V2**](ThreeDSecureDataV1V2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


