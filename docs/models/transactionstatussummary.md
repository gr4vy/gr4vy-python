# TransactionStatusSummary


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `type`                                                     | *Optional[Literal["transaction"]]*                         | :heavy_minus_sign:                                         | Always `transaction`.                                      | transaction                                                |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | The ID for the transaction.                                | 7099948d-7286-47e4-aad8-b68f7eb44591                       |
| `status`                                                   | [models.TransactionStatus](../models/transactionstatus.md) | :heavy_check_mark:                                         | N/A                                                        |                                                            |