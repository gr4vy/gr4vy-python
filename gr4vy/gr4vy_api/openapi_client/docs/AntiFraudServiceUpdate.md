# AntiFraudServiceUpdate

A request to update an anti-fraud service.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_fraud_service_definition_id** | **str** | The name of the Anti-Fraud service provider. During update request, this value is used for validation only but the underlying service can not be changed for an existing service. | 
**display_name** | **str** | A unique name for this anti-fraud service which is used in the Gr4vy admin panel to give a anti-fraud Service a human readable name. | [optional] 
**active** | **bool** | Defines if this service is currently active or not. | [optional]  if omitted the server will use the default value of True
**fields** | [**[AntiFraudServiceUpdateFields]**](AntiFraudServiceUpdateFields.md) | A list of fields, each containing a key-value pair for each field defined by the definition for this anti-fraud service e.g. for Sift &#x60;api_key&#x60; must be sent within this field when creating the service.  For updates, only the fields sent here will be updated, existing ones will not be affected if not present. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


