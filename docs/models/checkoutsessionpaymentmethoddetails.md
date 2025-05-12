# CheckoutSessionPaymentMethodDetails


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `bin`                                                      | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The first 6 digit of the card.                             | 411111                                                     |
| `card_country`                                             | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The country of the card issuer.                            | US                                                         |
| `card_type`                                                | [OptionalNullable[models.CardType]](../models/cardtype.md) | :heavy_minus_sign:                                         | The payment scheme of the card.                            |                                                            |
| `card_issuer_name`                                         | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The card issuer.                                           | Bank of America NA                                         |