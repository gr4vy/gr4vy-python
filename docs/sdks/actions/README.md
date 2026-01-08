# Transactions.Actions

## Overview

### Available Operations

* [list](#list) - List transaction Flow rules

## list

Retrieve the list of Flow rule actions that have been triggered for a transaction.

### Example Usage

<!-- UsageSnippet language="python" operationID="list_transaction_actions" method="get" path="/transactions/{transaction_id}/actions" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.transactions.actions.list(transaction_id="7099948d-7286-47e4-aad8-b68f7eb44591")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transaction_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ID of the transaction                                           | 7099948d-7286-47e4-aad8-b68f7eb44591                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TransactionActions](../../models/transactionactions.md)**

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