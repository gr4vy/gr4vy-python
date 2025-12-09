# PaymentMethods.NetworkTokens.Cryptogram

## Overview

### Available Operations

* [create](#create) - Provision network token cryptogram

## create

Provision a cryptogram for a network token.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_payment_method_network_token_cryptogram" method="post" path="/payment-methods/{payment_method_id}/network-tokens/{network_token_id}/cryptogram" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payment_methods.network_tokens.cryptogram.create(payment_method_id="ef9496d8-53a5-4aad-8ca2-00eb68334389", network_token_id="f8dd5cfc-7834-4847-95dc-f75a360e2298", merchant_initiated=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_method_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the payment method                                        | ef9496d8-53a5-4aad-8ca2-00eb68334389                                |
| `network_token_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the network token                                         | f8dd5cfc-7834-4847-95dc-f75a360e2298                                |
| `merchant_initiated`                                                | *bool*                                                              | :heavy_check_mark:                                                  | Defines if the request is merchant initiated or not.                | false                                                               |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Cryptogram](../../models/cryptogram.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.Error400            | 400                        | application/json           |
| errors.Error401            | 401                        | application/json           |
| errors.Error403            | 403                        | application/json           |
| errors.Error404            | 404                        | application/json           |
| errors.Error405            | 405                        | application/json           |
| errors.Error409            | 409                        | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.Error425            | 425                        | application/json           |
| errors.Error429            | 429                        | application/json           |
| errors.Error500            | 500                        | application/json           |
| errors.Error502            | 502                        | application/json           |
| errors.Error504            | 504                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |