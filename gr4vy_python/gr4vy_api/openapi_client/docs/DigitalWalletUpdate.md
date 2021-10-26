# DigitalWalletUpdate

Request body to update a registered digital wallet's details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_name** | **str** | The name of the merchant. This is used to update the value initially used to register with a digital wallet provider and this name is not displayed to the buyer. | [optional] 
**domain_names** | **[str]** | The list of fully qualified domain names that a digital wallet provider should process payments for. | [optional] 
**environments** | **[str]** | Determines the Gr4vy environments in which this digital wallet should be available. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


