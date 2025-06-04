# Events
(*transactions.events*)

## Overview

### Available Operations

* [list](#list) - List transaction events

## list

Fetch a list of events for a transaction.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.transactions.events.list(transaction_id="7099948d-7286-47e4-aad8-b68f7eb44591", cursor="ZXhhbXBsZTE", limit=100)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transaction_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 7099948d-7286-47e4-aad8-b68f7eb44591                                |
| `cursor`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | A pointer to the page of results to return.                         | ZXhhbXBsZTE                                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of items that are at returned.                   | 100                                                                 |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TransactionEvents](../../models/transactionevents.md)**

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