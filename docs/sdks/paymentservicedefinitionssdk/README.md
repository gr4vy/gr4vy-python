# PaymentServiceDefinitionsSDK
(*payment_service_definitions*)

## Overview

### Available Operations

* [list](#list) - List payment service definitions
* [get](#get) - Get a payment service definition
* [session](#session) - Create a session for apayment service definition

## list

List the definitions of each payment service that can be configured.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payment_service_definitions.list(cursor="ZXhhbXBsZTE", limit=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cursor`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | A pointer to the page of results to return.                         | ZXhhbXBsZTE                                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of items that are at returned.                   | 20                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListPaymentServiceDefinitionsResponse](../../models/listpaymentservicedefinitionsresponse.md)**

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

Get the definition of a payment service that can be configured.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payment_service_definitions.get(payment_service_definition_id="adyen-ideal")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_service_definition_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | adyen-ideal                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PaymentServiceDefinition](../../models/paymentservicedefinition.md)**

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

## session

Creates a session for a payment service that supports sessions.

### Example Usage

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.payment_service_definitions.session(payment_service_definition_id="adyen-ideal", request_body={

    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_service_definition_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | adyen-ideal                                                         |
| `request_body`                                                      | Dict[str, *Any*]                                                    | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CreateSession](../../models/createsession.md)**

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