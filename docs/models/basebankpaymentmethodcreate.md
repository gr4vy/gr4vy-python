# BaseBankPaymentMethodCreate

Base class for Bank Payment Methods.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `method`                                                   | *Optional[Literal["bank"]]*                                | :heavy_minus_sign:                                         | Always `bank`.                                             | bank                                                       |
| `account_holder`                                           | [models.BankAccountHolder](../models/bankaccountholder.md) | :heavy_check_mark:                                         | N/A                                                        |                                                            |
| `buyer_id`                                                 | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The ID of the buyer to attach the method to.               | fe26475d-ec3e-4884-9553-f7356683f7f9                       |
| `buyer_external_identifier`                                | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The merchant reference for this payment method.            | payment-method-12345                                       |
| `external_identifier`                                      | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The merchant identifier for this payment method.           | payment-method-12345                                       |