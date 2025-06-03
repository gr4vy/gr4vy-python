# RegisterDigitalWalletDomainRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `digital_wallet_id`                                            | *str*                                                          | :heavy_check_mark:                                             | The ID of the digital wallet to remove a domain for.           | 1808f5e6-b49c-4db9-94fa-22371ea352f5                           |
| `merchant_account_id`                                          | *Optional[str]*                                                | :heavy_minus_sign:                                             | The ID of the merchant account to use for this request.        | default                                                        |
| `digital_wallet_domain`                                        | [models.DigitalWalletDomain](../models/digitalwalletdomain.md) | :heavy_check_mark:                                             | N/A                                                            |                                                                |