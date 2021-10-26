# Status

In many cases the Gr4vy API returns asynchronously, kicking off a job to create an authorization or a transaction, and returning a `Status` object with the ID of the pending object. The ID of this resource can be used to query an objects status, or additionally the client can use Pub/Sub to subscribe to the creation of the pending object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this object. This is always &#x60;status&#x60;. | [optional]  if omitted the server will use the default value of "status"
**status** | **str** | The status of this resource being created. This is always &#x60;pending&#x60;. | [optional]  if omitted the server will use the default value of "pending"
**resource_type** | **str** | The type of the object that is pending.  | [optional] 
**resource_id** | **str** | The ID of the object for which this status has been created. | [optional] 
**external_identifier** | **str, none_type** | An external identifier that can be used to match the record against your own records. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


