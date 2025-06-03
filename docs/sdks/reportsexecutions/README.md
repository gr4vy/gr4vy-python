# ReportsExecutions
(*reports_executions*)

## Overview

### Available Operations

* [list](#list) - List executed reports
* [get](#get) - Get executed report

## list

List all executed reports that have been generated.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.reports_executions.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor`                                                                                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                      | A pointer to the page of results to return.                                                                                                                                                                                                             | ZXhhbXBsZTE                                                                                                                                                                                                                                             |
| `limit`                                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | The maximum number of items that are at returned.                                                                                                                                                                                                       | 20                                                                                                                                                                                                                                                      |
| `report_name`                                                                                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                      | Filters the reports by searching their name for (partial) matches.                                                                                                                                                                                      | My report                                                                                                                                                                                                                                               |
| `created_at_lte`                                                                                                                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                      | Filters the results to only reports created before this ISO date-time string. The time zone must be included. Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`. | 2022-01-01T12:00:00+08:00                                                                                                                                                                                                                               |
| `created_at_gte`                                                                                                                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                      | Filters the results to only reports created after this ISO date-time string. The time zone must be included. Ensure that the date-time string is URL encoded, e.g. `2022-01-01T12:00:00+08:00` must be encoded as `2022-01-01T12%3A00%3A00%2B08%3A00`.  | 2022-01-01T12:00:00+08:00                                                                                                                                                                                                                               |
| `status`                                                                                                                                                                                                                                                | List[[models.ReportExecutionStatus](../../models/reportexecutionstatus.md)]                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                      | Filters the results to only the reports that have a `status` that matches with any of the provided status values.                                                                                                                                       | succeeded                                                                                                                                                                                                                                               |
| `creator_id`                                                                                                                                                                                                                                            | List[*str*]                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                      | Filters the results to only the reports that were created by the users with these IDs.                                                                                                                                                                  | 30362ed1-05cf-4a4c-8b4a-e76323df5f1e                                                                                                                                                                                                                    |
| `merchant_account_id`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | The ID of the merchant account to use for this request.                                                                                                                                                                                                 | default                                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                     |                                                                                                                                                                                                                                                         |

### Response

**[models.ReportExecutions](../../models/reportexecutions.md)**

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

## get

Fetch a specific executed report.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.reports_executions.get(report_execution_id="003bc416-f32a-420c-8eb2-062a386e1fb0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `report_execution_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The ID of the execution of a report to retrieve details for.        | 003bc416-f32a-420c-8eb2-062a386e1fb0                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ReportExecution](../../models/reportexecution.md)**

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