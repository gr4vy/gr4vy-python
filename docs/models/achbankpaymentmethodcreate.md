# ACHBankPaymentMethodCreate

ACH Bank Payment Method

Bank Payment Method for ACH bank accounts.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `method`                                                   | *Optional[Literal["bank"]]*                                | :heavy_minus_sign:                                         | Always `bank`.                                             | bank                                                       |
| `account_holder`                                           | [models.BankAccountHolder](../models/bankaccountholder.md) | :heavy_check_mark:                                         | N/A                                                        |                                                            |
| `buyer_id`                                                 | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The ID of the buyer to attach the method to.               | fe26475d-ec3e-4884-9553-f7356683f7f9                       |
| `buyer_external_identifier`                                | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The merchant reference for this payment method.            | payment-method-12345                                       |
| `external_identifier`                                      | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The merchant identifier for this payment method.           | payment-method-12345                                       |
| `scheme`                                                   | *Optional[Literal["ach"]]*                                 | :heavy_minus_sign:                                         | Always `ach`.                                              | ach                                                        |
| `account_number`                                           | *str*                                                      | :heavy_check_mark:                                         | The account number for this ACH bank account               | 123456789                                                  |
| `routing_number`                                           | *str*                                                      | :heavy_check_mark:                                         | The routing number for this ACH bank account               | 000000111                                                  |
| `is_tokenized`                                             | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Whether the account number is tokenized                    | false                                                      |
| `account_type`                                             | [models.AccountType](../models/accounttype.md)             | :heavy_check_mark:                                         | Specify whether this is a `checking` or `savings` account  | checking                                                   |