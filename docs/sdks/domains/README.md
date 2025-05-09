# Domains
(*digital_wallets.domains*)

## Overview

### Available Operations

* [create](#create) - Register a digital wallet domain
* [delete](#delete) - Remove a digital wallet domain

## create

Register a digital wallet domain (Apple Pay only).

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    server="sandbox",
    id="example",
    bearer_auth=auth.with_token(open("./private_key.pem").read(), expires_in=1),
    merchant_account_id="default",
) as g_client:

    res = g_client.digital_wallets.domains.create(digital_wallet_id="1808f5e6-b49c-4db9-94fa-22371ea352f5", domain_name="example.com", merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `digital_wallet_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the digital wallet to remove a domain for.                | 1808f5e6-b49c-4db9-94fa-22371ea352f5                                |
| `domain_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The domain to add or remove.                                        | example.com                                                         |
| `timeout_in_seconds`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.Error400            | 400                        | application/json           |
| errors.Error401            | 401                        | application/json           |
| errors.Error403            | 403                        | application/json           |
| errors.Error403Forbidden   | 403                        | application/json           |
| errors.Error403Active      | 403                        | application/json           |
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

## delete

Remove a digital wallet domain (Apple Pay only).

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    server="sandbox",
    id="example",
    bearer_auth=auth.with_token(open("./private_key.pem").read(), expires_in=1),
    merchant_account_id="default",
) as g_client:

    res = g_client.digital_wallets.domains.delete(digital_wallet_id="", domain_name="example.com", merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `digital_wallet_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `domain_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The domain to add or remove.                                        | example.com                                                         |
| `timeout_in_seconds`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.Error400            | 400                        | application/json           |
| errors.Error401            | 401                        | application/json           |
| errors.Error403            | 403                        | application/json           |
| errors.Error403Forbidden   | 403                        | application/json           |
| errors.Error403Active      | 403                        | application/json           |
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