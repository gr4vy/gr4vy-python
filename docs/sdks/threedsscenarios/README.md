# ThreeDsScenarios

## Overview

### Available Operations

* [create](#create) - Create a 3DS scenario
* [list](#list) - List 3DS scenario
* [update](#update) - Update a 3DS scenario
* [delete](#delete) - Delete a 3DS scenario

## create

Create a new 3DS scenario for a merchant account. Only available in sandbox environments.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_three_ds_scenario" method="post" path="/three-ds-scenarios" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.three_ds_scenarios.create(conditions={}, outcome={
        "version": "2.2.0",
        "authentication": {
            "transaction_status": "Y",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `conditions`                                                                            | [models.ThreeDSecureScenarioConditions](../../models/threedsecurescenarioconditions.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |                                                                                         |
| `outcome`                                                                               | [models.ThreeDSecureScenarioOutcome](../../models/threedsecurescenariooutcome.md)       | :heavy_check_mark:                                                                      | N/A                                                                                     |                                                                                         |
| `merchant_account_id`                                                                   | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | The ID of the merchant account to use for this request.                                 | default                                                                                 |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[models.ThreeDSecureScenario](../../models/threedsecurescenario.md)**

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

## list

List all 3DS scenarios for a merchant account. Only available in sandbox environments.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_three_ds_scenario" method="get" path="/three-ds-scenarios" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.three_ds_scenarios.list(limit=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cursor`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | A pointer to the page of results to return.                         | ZXhhbXBsZTE                                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of items that are at returned.                   | 20                                                                  |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetThreeDsScenarioResponse](../../models/getthreedsscenarioresponse.md)**

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

## update

Update a 3DS scenario. Only available in sandbox environments.

### Example Usage

<!-- UsageSnippet language="python" operationID="update_three_ds_scenario" method="put" path="/three-ds-scenarios/{three_ds_scenario_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.three_ds_scenarios.update(three_ds_scenario_id="7099948d-7286-47e4-aad8-b68f7eb44591")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `three_ds_scenario_id`                                                                                    | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The ID of the 3DS scenario                                                                                | 7099948d-7286-47e4-aad8-b68f7eb44591                                                                      |
| `merchant_account_id`                                                                                     | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | The ID of the merchant account to use for this request.                                                   | default                                                                                                   |
| `conditions`                                                                                              | [OptionalNullable[models.ThreeDSecureScenarioConditions]](../../models/threedsecurescenarioconditions.md) | :heavy_minus_sign:                                                                                        | Conditions for the scenario.                                                                              |                                                                                                           |
| `outcome`                                                                                                 | [OptionalNullable[models.ThreeDSecureScenarioOutcome]](../../models/threedsecurescenariooutcome.md)       | :heavy_minus_sign:                                                                                        | Outcome for the scenario.                                                                                 |                                                                                                           |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Response

**[models.ThreeDSecureScenario](../../models/threedsecurescenario.md)**

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

## delete

Removes a 3DS scenario from our system. Only available in sandbox environments.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_three_ds_scenario" method="delete" path="/three-ds-scenarios/{three_ds_scenario_id}" -->
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    g_client.three_ds_scenarios.delete(three_ds_scenario_id="7099948d-7286-47e4-aad8-b68f7eb44591")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `three_ds_scenario_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The ID of the 3DS scenario                                          | 7099948d-7286-47e4-aad8-b68f7eb44591                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

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