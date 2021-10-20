# APIKeyPair

Details about an API key pair.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;api-key-pair&#x60;. | [optional]  if omitted the server will use the default value of "api-key-pair"
**id** | **str** | A unique ID for this key-pair. This ID is the thumbprint of the key. | [optional] 
**private_key** | **str, none_type** | The private key for the key-pair. This is only returned after the key is initially requested. For subsequent API calls this value is &#x60;null&#x60;. | [optional] 
**created_at** | **datetime** | The date and time when this key pair was created. | [optional] 
**updated_at** | **datetime** | The date and time when this key pair was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


