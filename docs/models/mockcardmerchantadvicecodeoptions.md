# MockCardMerchantAdviceCodeOptions


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `result`                                                                           | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | The MAC to return for this request.                                                |
| `account_number`                                                                   | *Nullable[str]*                                                                    | :heavy_check_mark:                                                                 | When set, the MAC is only returned if the card number matches this account number. |