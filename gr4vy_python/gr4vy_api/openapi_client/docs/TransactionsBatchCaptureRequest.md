# TransactionsBatchCaptureRequest

A request to capture multiple previously authorized transactions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The (partial) amount to capture.  When left blank, this will capture the entire amount. | 
**currency** | **str** | A supported ISO-4217 currency code.  | 
**transaction_id** | **str** | The ID of the transaction to capture. | 
**external_identifier** | **str** | An external identifier that can be used to match the transaction against your own records. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


