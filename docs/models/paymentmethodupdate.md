# PaymentMethodUpdate

Request body for updating a stored payment method.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `expiration_date`                                                                | *OptionalNullable[str]*                                                          | :heavy_minus_sign:                                                               | The new expiration date for the payment method.                                  | 12/30                                                                            |
| `scheme_transaction_id`                                                          | *OptionalNullable[str]*                                                          | :heavy_minus_sign:                                                               | A scheme transaction identifier to associate with this payment method.           | 123456789012345                                                                  |
| `scheme_transaction_id_scheme`                                                   | [OptionalNullable[models.CardScheme]](../models/cardscheme.md)                   | :heavy_minus_sign:                                                               | The scheme associated with scheme_transaction_id. Only applies to card payments. | visa                                                                             |