# CaptureTransactionRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `transaction_id`                                             | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `timeout_in_seconds`                                         | *Optional[float]*                                            | :heavy_minus_sign:                                           | N/A                                                          |
| `merchant_account_id`                                        | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | The ID of the merchant account to use for this request.      |
| `transaction_capture`                                        | [models.TransactionCapture](../models/transactioncapture.md) | :heavy_check_mark:                                           | N/A                                                          |