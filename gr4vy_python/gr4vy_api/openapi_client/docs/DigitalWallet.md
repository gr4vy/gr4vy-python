# DigitalWallet

A digital wallet (e.g. Apple Pay) that has been registered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;digital-wallet&#x60;. | [optional]  if omitted the server will use the default value of "digital-wallet"
**provider** | **str** | The name of the digital wallet provider. | [optional]  if omitted the server will use the default value of "apple"
**id** | **str** | The ID of the registered digital wallet. | [optional] 
**merchant_name** | **str** | The name of the merchant the digital wallet is registered to. | [optional] 
**merchant_url** | **str, none_type** | The main URL of the merchant. | [optional]  if omitted the server will use the default value of "null"
**domain_names** | **[str]** | The list of fully qualified domain names that a digital wallet provider processes payments for. | [optional] 
**created_at** | **datetime** | The date and time when this digital wallet was registered. | [optional] 
**updated_at** | **datetime** | The date and time when this digital wallet was last updated. | [optional] 
**environments** | **[str]** | The Gr4vy environments in which this digital wallet is available. | [optional]  if omitted the server will use the default value of ["production"]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


