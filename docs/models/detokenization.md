# Detokenization


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `type`                                                                     | *Optional[Literal["payment-method-detokenization"]]*                       | :heavy_minus_sign:                                                         | Always `payment-method-detokenization`.                                    | payment-method-detokenization                                              |
| `encrypted_payload`                                                        | *str*                                                                      | :heavy_check_mark:                                                         | The card details, encrypted to the merchant's public key as a compact JWE. | eyJhbGciOiJSU0EtT0FFUC0yNTYiLCJlbmMiOi...                                  |