# ListThreeDsConfigurationsRequest


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `merchant_account_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The ID of the merchant account.                                     | merchant-12345                                                      |
| `currency`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | ISO 4217 currency code (3 characters) to filter 3DS configurations. | USD                                                                 |