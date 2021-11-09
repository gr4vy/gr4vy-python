# TokenizedRequest

Details for a previously tokenized payment method.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A ID that represents a previously tokenized payment method. This token can represent any type of payment method. | 
**method** | **str** | &#x60;id&#x60;. | defaults to "id"
**redirect_url** | **str** | We strongly recommended providing a &#x60;redirect_url&#x60; for stored cards when 3-D Secure is enabled and &#x60;three_d_secure_data&#x60; is not provided. This will be appended with both a transaction ID and status (e.g. &#x60;https://example.com/callback? gr4vy_transaction_id&#x3D;123&amp;gr4vy_transaction_status&#x3D;capture_succeeded&#x60;) after 3-D Secure has completed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


