# TransactionGiftCard


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `type`                                                     | *Optional[Literal["gift-card"]]*                           | :heavy_minus_sign:                                         | Always `gift-card`.                                        | gift-card                                                  |
| `id`                                                       | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The ID for the gift card.                                  | 356d56e5-fe16-42ae-97ee-8d55d846ae2e                       |
| `bin`                                                      | *str*                                                      | :heavy_check_mark:                                         | The first 6 digits of the full gift card number.           | 412345                                                     |
| `sub_bin`                                                  | *str*                                                      | :heavy_check_mark:                                         | The 3 digits after the `bin` of the full gift card number. | 554                                                        |
| `last4`                                                    | *str*                                                      | :heavy_check_mark:                                         | The last 4 digits for the gift card.                       | 1234                                                       |