# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;user&#x60;. | [optional]  if omitted the server will use the default value of "user"
**id** | **str** | The unique Gr4vy ID for this user. | [optional] 
**name** | **str** | The full name of this user. | [optional] 
**email_adress** | **str** | The email address for this user. | [optional] 
**has_valid_password** | **bool** | The user has set a valid password. | [optional] 
**reset_token** | **str, none_type** | The token required when setting a password. | [optional] 
**reset_token_expires_at** | **datetime, none_type** | The expiration date for the reset token. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


