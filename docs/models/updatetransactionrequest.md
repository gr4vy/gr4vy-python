# UpdateTransactionRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `transaction_id`                                           | *str*                                                      | :heavy_check_mark:                                         | The ID of the transaction                                  | 7099948d-7286-47e4-aad8-b68f7eb44591                       |
| `merchant_account_id`                                      | *Optional[str]*                                            | :heavy_minus_sign:                                         | The ID of the merchant account to use for this request.    | default                                                    |
| `transaction_update`                                       | [models.TransactionUpdate](../models/transactionupdate.md) | :heavy_check_mark:                                         | N/A                                                        |                                                            |