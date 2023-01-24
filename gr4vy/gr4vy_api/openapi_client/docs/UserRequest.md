# UserRequest

A request to create a user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The full name of the user which is used in the Gr4vy admin panel to give an user a human readable name. | [optional] 
**email_address** | **str** | The email address for this user. | [optional] 
**role_ids** | **[str]** | A list of role ids that will be assigned to the user being created. The creator must have &#x60;roles.write&#x60; or the role that is being assigned. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


