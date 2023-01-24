# Connection

A configured connection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the connection. | [optional] 
**type** | **str** | &#x60;connection&#x60;. | [optional]  if omitted the server will use the default value of "connection"
**name** | **str** | The name of this connection. | [optional] 
**active** | **bool** | Whether this connection is currently in use. Connections can be deactivated to allow for them to be kept around and re-activated at a later date. | [optional] 
**definition** | [**ConnectionDefinition**](ConnectionDefinition.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


