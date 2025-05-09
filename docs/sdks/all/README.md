# All
(*transactions.refunds.all*)

## Overview

### Available Operations

* [create](#create) - Create batch transaction refund

## create

Create a refund for all instruments on a transaction.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.transactions.refunds.all.create(transaction_id="7099948d-7286-47e4-aad8-b68f7eb44591", merchant_account_id="default", reason="Refund due to user request.", external_identifier="refund-12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `transaction_id`                                                                       | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    | 7099948d-7286-47e4-aad8-b68f7eb44591                                                   |
| `timeout_in_seconds`                                                                   | *Optional[float]*                                                                      | :heavy_minus_sign:                                                                     | N/A                                                                                    |                                                                                        |
| `merchant_account_id`                                                                  | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The ID of the merchant account to use for this request.                                | default                                                                                |
| `reason`                                                                               | *OptionalNullable[str]*                                                                | :heavy_minus_sign:                                                                     | An optional reason to attach extra context to the refund requests.                     | Refund due to user request.                                                            |
| `external_identifier`                                                                  | *OptionalNullable[str]*                                                                | :heavy_minus_sign:                                                                     | An external identifier that can be used to match the refunds against your own records. | refund-12345                                                                           |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[models.CollectionNoCursorRefund](../../models/collectionnocursorrefund.md)**

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