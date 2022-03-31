# DigitalWallet

A digital wallet (e.g. Apple Pay) that has been registered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;digital-wallet&#x60;. | [optional]  if omitted the server will use the default value of "digital-wallet"
**provider** | **str** | The name of the digital wallet provider. | [optional] 
**id** | **str** | The ID of the registered digital wallet. | [optional] 
**merchant_name** | **str** | The name of the merchant the digital wallet is registered to. | [optional] 
**merchant_url** | **str, none_type** | The main URL of the merchant. | [optional]  if omitted the server will use the default value of "null"
**domain_names** | **[str]** | The list of domain names that a digital wallet can be used on. To use a digital wallet on a website, the domain of the site is required to be in this list. | [optional] 
**created_at** | **datetime** | The date and time when this digital wallet was registered. | [optional] 
**updated_at** | **datetime** | The date and time when this digital wallet was last updated. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


