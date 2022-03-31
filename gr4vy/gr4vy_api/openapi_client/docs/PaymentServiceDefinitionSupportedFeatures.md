# PaymentServiceDefinitionSupportedFeatures

Features supported by the payment definition.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_tokenization** | **bool** | Supports storing a payment method via tokenization. | [optional] 
**three_d_secure_hosted** | **bool** | Supports hosted 3-D Secure with a redirect. | [optional] 
**three_d_secure_pass_through** | **bool** | Supports passing 3-D Secure data to the underlying processor. | [optional] 
**network_tokens** | **bool** | Supports passing decrypted digital wallet (e.g. Apple Pay) tokens to the underlying processor. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


