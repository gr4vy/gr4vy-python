# PaymentServices
(*payment_services*)

## Overview

### Available Operations

* [list](#list) - List payment services
* [create](#create) - Update a configured payment service
* [get](#get) - Get payment service
* [update](#update) - Configure a payment service
* [delete](#delete) - Delete a configured payment service
* [verify](#verify) - Verify payment service credentials
* [session](#session) - Create a session for apayment service definition

## list

List the configured payment services.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_services.list(cursor="ZXhhbXBsZTE", deleted=True, merchant_account_id="default")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `method`                                                            | [OptionalNullable[models.Method]](../../models/method.md)           | :heavy_minus_sign:                                                  | Return any payment service for this method.                         |                                                                     |
| `cursor`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | A pointer to the page of results to return.                         | ZXhhbXBsZTE                                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The maximum number of items that are at returned.                   | 20                                                                  |
| `deleted`                                                           | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | Return any deleted payment service.                                 | true                                                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListPaymentServicesResponse](../../models/listpaymentservicesresponse.md)**

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

## create

Updates the configuration of a payment service.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_services.create(display_name="Stripe", payment_service_definition_id="stripe-card", fields=[
        {
            "key": "api_key",
            "value": "key-12345",
        },
    ], accepted_currencies=[
        "EUR",
        "GBP",
        "USD",
    ], accepted_countries=[
        "DE",
        "GB",
        "US",
    ], merchant_account_id="default", reporting_fields=[
        {
            "key": "api_key",
            "value": "key-12345",
        },
        {
            "key": "api_key",
            "value": "key-12345",
        },
    ], position=1, active=True, merchant_profile={
        "key": {
            "merchant_acquirer_bin": "516327",
            "merchant_url": "https://example.com",
            "merchant_acquirer_id": "123456789012345",
            "merchant_name": "Acme Inc.",
            "merchant_country_code": "USD",
            "merchant_category_code": "1234",
        },
    }, payment_method_tokenization_enabled=True, network_tokens_enabled=True, open_loop=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `display_name`                                                                                                                                | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The display name for the payment service.                                                                                                     | Stripe                                                                                                                                        |
| `payment_service_definition_id`                                                                                                               | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The definition ID of the service to configure.                                                                                                | stripe-card                                                                                                                                   |
| `fields`                                                                                                                                      | List[[models.FieldT](../../models/fieldt.md)]                                                                                                 | :heavy_check_mark:                                                                                                                            | The non-secret credential fields that have been configured for this payment service. Any secret fields are omitted.                           |                                                                                                                                               |
| `accepted_currencies`                                                                                                                         | List[*str*]                                                                                                                                   | :heavy_check_mark:                                                                                                                            | A list of currencies for which this service is enabled, in ISO 4217 three-letter code format.                                                 | [<br/>"USD",<br/>"EUR",<br/>"GBP"<br/>]                                                                                                       |
| `accepted_countries`                                                                                                                          | List[*str*]                                                                                                                                   | :heavy_check_mark:                                                                                                                            | A list of countries for which this service is enabled, in ISO two-letter code format.                                                         | [<br/>"US",<br/>"DE",<br/>"GB"<br/>]                                                                                                          |
| `merchant_account_id`                                                                                                                         | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The ID of the merchant account to use for this request.                                                                                       | default                                                                                                                                       |
| `reporting_fields`                                                                                                                            | List[[models.FieldT](../../models/fieldt.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                            | The non-secret reporting fields that have been configured for this payment service. Any secret fields are omitted.                            |                                                                                                                                               |
| `position`                                                                                                                                    | *OptionalNullable[int]*                                                                                                                       | :heavy_minus_sign:                                                                                                                            | Deprecated field used to define the order in which to process payment services                                                                | 1                                                                                                                                             |
| `active`                                                                                                                                      | *OptionalNullable[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                            | Defines if this payment service is currently active.                                                                                          | true                                                                                                                                          |
| `three_d_secure_enabled`                                                                                                                      | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Defines if this payment service has 3DS enabled.                                                                                              | true                                                                                                                                          |
| `merchant_profile`                                                                                                                            | Dict[str, [Nullable[models.MerchantProfileScheme]](../../models/merchantprofilescheme.md)]                                                    | :heavy_minus_sign:                                                                                                                            | An object containing a key for each supported card schemes, and for each key an object with the 3DS profile for this service for that scheme. |                                                                                                                                               |
| `payment_method_tokenization_enabled`                                                                                                         | *OptionalNullable[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                            | Defines if this payment service support payment method tokenization.                                                                          | true                                                                                                                                          |
| `network_tokens_enabled`                                                                                                                      | *OptionalNullable[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                            | Defines if this payment service supports network tokens.                                                                                      | true                                                                                                                                          |
| `open_loop`                                                                                                                                   | *OptionalNullable[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                            | Defines if this payment service is open loop.                                                                                                 | true                                                                                                                                          |
| `settlement_reporting_enabled`                                                                                                                | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Defines if this payment service has settlement reporting enabled.                                                                             | true                                                                                                                                          |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.PaymentService](../../models/paymentservice.md)**

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

## get

Get the details of a configured payment service.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_services.get(payment_service_id="fffd152a-9532-4087-9a4f-de58754210f0", merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_service_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | the ID of the payment service                                       | fffd152a-9532-4087-9a4f-de58754210f0                                |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PaymentService](../../models/paymentservice.md)**

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

## update

Configures a new payment service for use by merchants.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_services.update(payment_service_id="fffd152a-9532-4087-9a4f-de58754210f0", merchant_account_id="default", display_name="Stripe", position=1, accepted_currencies=[
        "EUR",
        "GBP",
        "USD",
    ], accepted_countries=[
        "DE",
        "GB",
        "US",
    ], active=False, three_d_secure_enabled=True, merchant_profile={
        "key": {
            "merchant_acquirer_bin": "516327",
            "merchant_url": "https://example.com",
            "merchant_acquirer_id": "123456789012345",
            "merchant_name": "Acme Inc.",
            "merchant_country_code": "USD",
            "merchant_category_code": "1234",
        },
        "key1": {
            "merchant_acquirer_bin": "516327",
            "merchant_url": "https://example.com",
            "merchant_acquirer_id": "123456789012345",
            "merchant_name": "Acme Inc.",
            "merchant_country_code": "USD",
            "merchant_category_code": "1234",
        },
    }, payment_method_tokenization_enabled=True, network_tokens_enabled=True, open_loop=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_service_id`                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | the ID of the payment service                                                                                                                 | fffd152a-9532-4087-9a4f-de58754210f0                                                                                                          |
| `merchant_account_id`                                                                                                                         | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The ID of the merchant account to use for this request.                                                                                       | default                                                                                                                                       |
| `display_name`                                                                                                                                | *OptionalNullable[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                            | The display name for the payment service.                                                                                                     | Stripe                                                                                                                                        |
| `fields`                                                                                                                                      | List[[models.VoidableField](../../models/voidablefield.md)]                                                                                   | :heavy_minus_sign:                                                                                                                            | The non-secret credential fields that have been configured for this payment service. Any secret fields are omitted.                           |                                                                                                                                               |
| `reporting_fields`                                                                                                                            | List[[models.VoidableField](../../models/voidablefield.md)]                                                                                   | :heavy_minus_sign:                                                                                                                            | The non-secret reporting fields that have been configured for this payment service. Any secret fields are omitted.                            |                                                                                                                                               |
| `position`                                                                                                                                    | *OptionalNullable[int]*                                                                                                                       | :heavy_minus_sign:                                                                                                                            | Deprecated field used to define the order in which to process payment services                                                                | 1                                                                                                                                             |
| `accepted_currencies`                                                                                                                         | List[*str*]                                                                                                                                   | :heavy_minus_sign:                                                                                                                            | A list of currencies for which this service is enabled, in ISO 4217 three-letter code format.                                                 | [<br/>"USD",<br/>"EUR",<br/>"GBP"<br/>]                                                                                                       |
| `accepted_countries`                                                                                                                          | List[*str*]                                                                                                                                   | :heavy_minus_sign:                                                                                                                            | A list of countries for which this service is enabled, in ISO two-letter code format.                                                         | [<br/>"US",<br/>"DE",<br/>"GB"<br/>]                                                                                                          |
| `active`                                                                                                                                      | *OptionalNullable[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                            | Defines if this payment service is currently active.                                                                                          | true                                                                                                                                          |
| `three_d_secure_enabled`                                                                                                                      | *OptionalNullable[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                            | Defines if this payment service has 3DS enabled.                                                                                              | true                                                                                                                                          |
| `merchant_profile`                                                                                                                            | Dict[str, [Nullable[models.MerchantProfileScheme]](../../models/merchantprofilescheme.md)]                                                    | :heavy_minus_sign:                                                                                                                            | An object containing a key for each supported card schemes, and for each key an object with the 3DS profile for this service for that scheme. |                                                                                                                                               |
| `payment_method_tokenization_enabled`                                                                                                         | *OptionalNullable[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                            | Defines if this payment service support payment method tokenization.                                                                          | true                                                                                                                                          |
| `network_tokens_enabled`                                                                                                                      | *OptionalNullable[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                            | Defines if this payment service supports network tokens.                                                                                      | true                                                                                                                                          |
| `open_loop`                                                                                                                                   | *OptionalNullable[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                            | Defines if this payment service is open loop.                                                                                                 | true                                                                                                                                          |
| `settlement_reporting_enabled`                                                                                                                | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Defines if this payment service has settlement reporting enabled.                                                                             | true                                                                                                                                          |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.PaymentService](../../models/paymentservice.md)**

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

Deletes all the configuration of a payment service.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_services.delete(payment_service_id="fffd152a-9532-4087-9a4f-de58754210f0", merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_service_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | the ID of the payment service                                       | fffd152a-9532-4087-9a4f-de58754210f0                                |
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

## verify

Verify the credentials of a configured payment service

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_services.verify(payment_service_definition_id="stripe-card", fields=[
        {
            "key": "api_key",
            "value": "key-12345",
        },
        {
            "key": "api_key",
            "value": "key-12345",
        },
        {
            "key": "api_key",
            "value": "key-12345",
        },
    ], merchant_account_id="default", payment_service_id="fffd152a-9532-4087-9a4f-de58754210f0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    | Example                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_service_definition_id`                                                                                                                | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | The ID of the payment service definition to verify the fields against                                                                          | stripe-card                                                                                                                                    |
| `fields`                                                                                                                                       | List[[models.FieldT](../../models/fieldt.md)]                                                                                                  | :heavy_check_mark:                                                                                                                             | The fields and their values, or a set of updated fields to merge with existing values.                                                         |                                                                                                                                                |
| `timeout_in_seconds`                                                                                                                           | *Optional[float]*                                                                                                                              | :heavy_minus_sign:                                                                                                                             | N/A                                                                                                                                            |                                                                                                                                                |
| `merchant_account_id`                                                                                                                          | *Optional[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                             | The ID of the merchant account to use for this request.                                                                                        | default                                                                                                                                        |
| `payment_service_id`                                                                                                                           | *OptionalNullable[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                             | The optional ID of the configured payment service. New fields will be merged with any existing fields already stored before they are verified. | fffd152a-9532-4087-9a4f-de58754210f0                                                                                                           |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |                                                                                                                                                |

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

## session

Creates a session for a payment service that supports sessions.

### Example Usage

```python
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.payment_services.session(payment_service_id="fffd152a-9532-4087-9a4f-de58754210f0", request_body={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, merchant_account_id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_service_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | the ID of the payment service                                       | fffd152a-9532-4087-9a4f-de58754210f0                                |
| `request_body`                                                      | Dict[str, *Any*]                                                    | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `merchant_account_id`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of the merchant account to use for this request.             | default                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CreateSession](../../models/createsession.md)**

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