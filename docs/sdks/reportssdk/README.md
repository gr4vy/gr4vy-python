# Reports

## Overview

### Available Operations

* [list](#list) - List configured reports
* [create](#create) - Add a report
* [get](#get) - Get a report
* [put](#put) - Update a report

## list

List all configured reports that can be generated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list_reports" method="get" path="/reports" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.reports.list(limit=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cursor`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | A pointer to the page of results to return.                         | ZXhhbXBsZTE                                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of items that are at returned.                   | 20                                                                  |
| `schedule`                                                          | List[[models.ReportSchedule](../../models/reportschedule.md)]       | :heavy_minus_sign:                                                  | Filters the reports by the type of schedule at which they run.      | [<br/>"daily",<br/>"monthly"<br/>]                                  |
| `schedule_enabled`                                                  | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | Filters the reports by wether their schedule is enabled.            | true                                                                |
| `name`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Filters the reports by searching their name for (partial) matches.  | My report                                                           |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListReportsResponse](../../models/listreportsresponse.md)**

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

## create

Create a new report.

### Example Usage

<!-- UsageSnippet language="python" operationID="add_report" method="post" path="/reports" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.reports.create(name="Monthly Transaction Report", schedule="daily", schedule_enabled=True, spec={
        "model": "detailed_settlement",
        "params": {
            "filters": {
                "ingested_at": {
                    "end": "day_end",
                    "start": "day_start",
                },
            },
        },
    }, schedule_timezone="UTC")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The name of the report.                                             | Monthly Transaction Report                                          |
| `schedule`                                                          | [models.ReportSchedule](../../models/reportschedule.md)             | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `schedule_enabled`                                                  | *bool*                                                              | :heavy_check_mark:                                                  | Whether the report schedule is enabled.                             | true                                                                |
| `spec`                                                              | [models.Spec](../../models/spec.md)                                 | :heavy_check_mark:                                                  | The report specification.                                           |                                                                     |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | A description of the report.                                        | Monthly transaction summary for May 2024.                           |
| `schedule_timezone`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The timezone for the report schedule.                               | UTC                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Report](../../models/report.md)**

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

Fetches a report by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_report" method="get" path="/reports/{report_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.reports.get(report_id="4d4c7123-b794-4fad-b1b9-5ab2606e6bbe")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `report_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The ID of the report to retrieve details for.                       | 4d4c7123-b794-4fad-b1b9-5ab2606e6bbe                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Report](../../models/report.md)**

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

## put

Updates the configuration of a report.

### Example Usage

<!-- UsageSnippet language="python" operationID="update_report" method="put" path="/reports/{report_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.reports.put(report_id="4d4c7123-b794-4fad-b1b9-5ab2606e6bbe")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `report_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The ID of the report to edit.                                       | 4d4c7123-b794-4fad-b1b9-5ab2606e6bbe                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `name`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | The name of the report.                                             | Monthly Transaction Report                                          |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | A description of the report.                                        | Monthly transaction summary for May 2024.                           |
| `schedule_enabled`                                                  | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | Whether the report schedule is enabled.                             | true                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Report](../../models/report.md)**

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