# AuditLog

A log of a change that occurred in the Gr4vy instance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;audit-log&#x60;. | [optional]  if omitted the server will use the default value of "audit-log"
**id** | **str** | The ID of the audit log entry. | [optional] 
**timestamp** | **str** | The date and time that the action was performed. | [optional] 
**action** | **str** | The action that was performed. | [optional] 
**user** | [**AuditLogUser**](AuditLogUser.md) |  | [optional] 
**resource** | [**AuditLogResource**](AuditLogResource.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


