# AuditLogs
(*audit_logs*)

## Overview

### Available Operations

* [list](#list) - List audit log entries

## list

Returns a list of activity by dashboard users.

### Example Usage

```python
from gr4vy import Gr4vy, models
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.audit_logs.list(cursor="ZXhhbXBsZTE", action=models.AuditLogAction.CREATED, user_id="14b7b8c5-a6ba-4fb6-bbab-52d43c7f37ef", resource_type="user")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `cursor`                                                                                                       | *OptionalNullable[str]*                                                                                        | :heavy_minus_sign:                                                                                             | A pointer to the page of results to return.                                                                    | ZXhhbXBsZTE                                                                                                    |
| `limit`                                                                                                        | *Optional[int]*                                                                                                | :heavy_minus_sign:                                                                                             | The maximum number of items that are at returned.                                                              | 20                                                                                                             |
| `action`                                                                                                       | [OptionalNullable[models.AuditLogAction]](../../models/auditlogaction.md)                                      | :heavy_minus_sign:                                                                                             | Filters the results to only the items for which the `audit-log` has an `action` that matches this value.       | created                                                                                                        |
| `user_id`                                                                                                      | *OptionalNullable[str]*                                                                                        | :heavy_minus_sign:                                                                                             | Filters the results to only the items for which the `user` has an `id` that matches this value.                | 14b7b8c5-a6ba-4fb6-bbab-52d43c7f37ef                                                                           |
| `resource_type`                                                                                                | *OptionalNullable[str]*                                                                                        | :heavy_minus_sign:                                                                                             | Filters the results to only the items for which the `audit-log` has a `resource` that matches this type value. | user                                                                                                           |
| `merchant_account_id`                                                                                          | *OptionalNullable[str]*                                                                                        | :heavy_minus_sign:                                                                                             | The ID of the merchant account to use for this request.                                                        |                                                                                                                |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |                                                                                                                |

### Response

**[models.ListAuditLogsResponse](../../models/listauditlogsresponse.md)**

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