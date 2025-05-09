# Jobs
(*account_updater.jobs*)

## Overview

### Available Operations

* [create](#create) - Create account updater job

## create

Schedule one or more stored cards for an account update.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.account_updater.jobs.create(payment_method_ids=[
        "ef9496d8-53a5-4aad-8ca2-00eb68334389",
        "f29e886e-93cc-4714-b4a3-12b7a718e595",
    ], merchant_account_id="default")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `payment_method_ids`                                                               | List[*str*]                                                                        | :heavy_check_mark:                                                                 | A list of payment method IDs to request an update for.                             | [<br/>"ef9496d8-53a5-4aad-8ca2-00eb68334389",<br/>"f29e886e-93cc-4714-b4a3-12b7a718e595"<br/>] |
| `timeout_in_seconds`                                                               | *Optional[float]*                                                                  | :heavy_minus_sign:                                                                 | N/A                                                                                |                                                                                    |
| `merchant_account_id`                                                              | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The ID of the merchant account to use for this request.                            | default                                                                            |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |                                                                                    |

### Response

**[models.AccountUpdaterJob](../../models/accountupdaterjob.md)**

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