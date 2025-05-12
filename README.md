# Gr4vy Python SDK (Beta)


Developer-friendly & type-safe Python SDK specifically catered to leverage *gr4vy* API.

<div align="left">
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gr4vy?style=for-the-badge">
    <a href="https://www.speakeasy.com/?utm_source=gr4vy&utm_campaign=python">
        <img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This is a Beta release of our latest SDK. Please refer to the [legacy Python SDK](https://github.com/gr4vy/gr4vy-python/tree/legacy) for the latest stable build.

<!-- Start Summary [summary] -->
## Summary

Gr4vy: The Gr4vy API.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [gr4vy](#gr4vy)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Merchant account ID selection](#merchant-account-id-selection)
* [Webhook payload and headers](#webhook-payload-and-headers)
* [Or when using async:](#or-when-using-async)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install gr4vy
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add gr4vy
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from gr4vy python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "gr4vy",
# ]
# ///

from gr4vy import Gr4vy

sdk = Gr4vy(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

## SDK Example Usage

### Example

```python
# Synchronous Example
from gr4vy import Gr4vy, auth
import os


with Gr4vy(
    id="example",
    server="production",
    merchant_account_id="default",
    bearer_auth=auth.with_token(open("./private_key.pem").read())
) as g_client:

    res = g_client.transactions.list()

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from gr4vy import Gr4vy
import os

async def main():

    async with Gr4vy(
        id="example",
        server="production",
        merchant_account_id="default",
        bearer_auth=auth.with_token(open("./private_key.pem").read())
    ) as g_client:
        res = await g_client.transactions.list()

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      | Environment Variable |
| ------------- | ---- | ----------- | -------------------- |
| `bearer_auth` | http | HTTP Bearer | `GR4VY_BEARER_AUTH`  |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from gr4vy import Gr4vy
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
<!-- End Authentication [security] -->

## Merchant account ID selection

Depending on the key used, you might need to explicitly define a merchant account ID to use. In our API, 
this uses the `X-GR4VY-MERCHANT-ACCOUNT-ID` header. When using the SDK, you can set the `merchant_account_id`
on every request.

``py
res = g_client.transactions.list(merchant_account_id: 'merchant-12345')
```

Alternatively, the merchant account ID can also be set when initializing the SDK.

```py
with Gr4vy(
    id="spider",
    merchant_account_id="merchant-12345",
    bearer_auth=auth.get_token(private_key)
) as g_client:
    response = g_client.transactions.list()
```

## Webhooks verification

The SDK makes it easy to verify that incoming webhooks were actually sent by Gr4vy. Once you have configured the webhook subscription with its corresponding secret, that can be verified the following way:

```py
from gr4vy.webhooks import verify_webhook

# Webhook payload and headers
payload = 'your-webhook-payload'
secret = 'your-webhook-secret'
signature_header = 'signatures-from-header'
timestamp_header = 'timestamp-from-header'
timestamp_tolerance = 300  # optional, in seconds (default: 0)

try:
    # Verify the webhook
    verify_webhook(
        payload=payload,
        secret=secret,
        signature_header=signature_header,
        timestamp_header=timestamp_header,
        timestamp_tolerance=timestamp_tolerance
    )
    print('Webhook verified successfully!')
except ValueError as error:
    print(f'Webhook verification failed: {error}')
```

### Parameters

- **`payload`**: The raw payload string received in the webhook request.
- **`secret`**: The secret used to sign the webhook. This is provided in your Gr4vy dashboard.
- **`signatureHeader`**: The `X-Gr4vy-Signature` header from the webhook request.
- **`timestampHeader`**: The `X-Gr4vy-Timestamp` header from the webhook request.
- **`timestampTolerance`**: _(Optional)_ The maximum allowed difference (in seconds) between the current time and the timestamp in the webhook. Defaults to `0` (no tolerance).



<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [account_updater](docs/sdks/accountupdater/README.md)


#### [account_updater.jobs](docs/sdks/jobs/README.md)

* [create](docs/sdks/jobs/README.md#create) - Create account updater job

### [audit_logs](docs/sdks/auditlogs/README.md)

* [list](docs/sdks/auditlogs/README.md#list) - List audit log entries

### [buyers](docs/sdks/buyers/README.md)

* [list](docs/sdks/buyers/README.md#list) - List all buyers
* [create](docs/sdks/buyers/README.md#create) - Add a buyer
* [get](docs/sdks/buyers/README.md#get) - Get a buyer
* [update](docs/sdks/buyers/README.md#update) - Update a buyer
* [delete](docs/sdks/buyers/README.md#delete) - Delete a buyer

#### [buyers.gift_cards](docs/sdks/buyersgiftcards/README.md)

* [list](docs/sdks/buyersgiftcards/README.md#list) - List gift cards for a buyer

#### [buyers.payment_methods](docs/sdks/buyerspaymentmethods/README.md)

* [list](docs/sdks/buyerspaymentmethods/README.md#list) - List payment methods for a buyer

#### [buyers.shipping_details](docs/sdks/buyersshippingdetails/README.md)

* [create](docs/sdks/buyersshippingdetails/README.md#create) - Add buyer shipping details
* [list](docs/sdks/buyersshippingdetails/README.md#list) - List a buyer's shipping details
* [get](docs/sdks/buyersshippingdetails/README.md#get) - Get buyer shipping details
* [update](docs/sdks/buyersshippingdetails/README.md#update) - Update a buyer's shipping details
* [delete](docs/sdks/buyersshippingdetails/README.md#delete) - Delete a buyer's shipping details

### [card_scheme_definitions](docs/sdks/cardschemedefinitions/README.md)

* [list](docs/sdks/cardschemedefinitions/README.md#list) - List card scheme definitions

### [checkout_sessions](docs/sdks/checkoutsessions/README.md)

* [create](docs/sdks/checkoutsessions/README.md#create) - Create checkout session
* [update](docs/sdks/checkoutsessions/README.md#update) - Update checkout session
* [get](docs/sdks/checkoutsessions/README.md#get) - Get checkout session
* [delete](docs/sdks/checkoutsessions/README.md#delete) - Delete checkout session

### [digital_wallets](docs/sdks/digitalwallets/README.md)

* [create](docs/sdks/digitalwallets/README.md#create) - Register digital wallet
* [list](docs/sdks/digitalwallets/README.md#list) - List digital wallets
* [get](docs/sdks/digitalwallets/README.md#get) - Get digital wallet
* [delete](docs/sdks/digitalwallets/README.md#delete) - Delete digital wallet
* [update](docs/sdks/digitalwallets/README.md#update) - Update digital wallet

#### [digital_wallets.domains](docs/sdks/domains/README.md)

* [create](docs/sdks/domains/README.md#create) - Register a digital wallet domain
* [delete](docs/sdks/domains/README.md#delete) - Remove a digital wallet domain

#### [digital_wallets.sessions](docs/sdks/sessions/README.md)

* [google_pay](docs/sdks/sessions/README.md#google_pay) - Create a Google Pay session
* [apple_pay](docs/sdks/sessions/README.md#apple_pay) - Create a Apple Pay session
* [click_to_pay](docs/sdks/sessions/README.md#click_to_pay) - Create a Click to Pay session

### [gift_cards](docs/sdks/giftcards/README.md)

* [get](docs/sdks/giftcards/README.md#get) - Get gift card
* [delete](docs/sdks/giftcards/README.md#delete) - Delete a gift card
* [create](docs/sdks/giftcards/README.md#create) - Create gift card
* [list](docs/sdks/giftcards/README.md#list) - List gift cards

#### [gift_cards.balances](docs/sdks/balances/README.md)

* [list](docs/sdks/balances/README.md#list) - List gift card balances


### [merchant_accounts](docs/sdks/merchantaccounts/README.md)

* [list](docs/sdks/merchantaccounts/README.md#list) - List all merchant accounts
* [create](docs/sdks/merchantaccounts/README.md#create) - Create a merchant account
* [get](docs/sdks/merchantaccounts/README.md#get) - Get a merchant account
* [update](docs/sdks/merchantaccounts/README.md#update) - Update a merchant account

### [payment_methods](docs/sdks/paymentmethods/README.md)

* [list](docs/sdks/paymentmethods/README.md#list) - List all payment methods
* [create](docs/sdks/paymentmethods/README.md#create) - Create payment method
* [get](docs/sdks/paymentmethods/README.md#get) - Get payment method
* [delete](docs/sdks/paymentmethods/README.md#delete) - Delete payment method

#### [payment_methods.network_tokens](docs/sdks/networktokens/README.md)

* [list](docs/sdks/networktokens/README.md#list) - List network tokens
* [create](docs/sdks/networktokens/README.md#create) - Provision network token
* [suspend](docs/sdks/networktokens/README.md#suspend) - Suspend network token
* [resume](docs/sdks/networktokens/README.md#resume) - Resume network token
* [delete](docs/sdks/networktokens/README.md#delete) - Delete network token

#### [payment_methods.network_tokens.cryptogram](docs/sdks/networktokenscryptogram/README.md)

* [create](docs/sdks/networktokenscryptogram/README.md#create) - Provision network token cryptogram

#### [payment_methods.payment_service_tokens](docs/sdks/paymentservicetokens/README.md)

* [list](docs/sdks/paymentservicetokens/README.md#list) - List payment service tokens
* [create](docs/sdks/paymentservicetokens/README.md#create) - Create payment service token
* [delete](docs/sdks/paymentservicetokens/README.md#delete) - Delete payment service token

### [payment_options](docs/sdks/paymentoptions/README.md)

* [list](docs/sdks/paymentoptions/README.md#list) - List payment options

### [payment_service_definitions](docs/sdks/paymentservicedefinitions/README.md)

* [list](docs/sdks/paymentservicedefinitions/README.md#list) - List payment service definitions
* [get](docs/sdks/paymentservicedefinitions/README.md#get) - Get a payment service definition
* [session](docs/sdks/paymentservicedefinitions/README.md#session) - Create a session for apayment service definition

### [payment_services](docs/sdks/paymentservices/README.md)

* [list](docs/sdks/paymentservices/README.md#list) - List payment services
* [create](docs/sdks/paymentservices/README.md#create) - Update a configured payment service
* [get](docs/sdks/paymentservices/README.md#get) - Get payment service
* [update](docs/sdks/paymentservices/README.md#update) - Configure a payment service
* [delete](docs/sdks/paymentservices/README.md#delete) - Delete a configured payment service
* [verify](docs/sdks/paymentservices/README.md#verify) - Verify payment service credentials
* [session](docs/sdks/paymentservices/README.md#session) - Create a session for apayment service definition

### [payouts](docs/sdks/payouts/README.md)

* [list](docs/sdks/payouts/README.md#list) - List payouts created.
* [create](docs/sdks/payouts/README.md#create) - Create a payout.
* [get](docs/sdks/payouts/README.md#get) - Get a payout.

### [refunds](docs/sdks/refunds/README.md)

* [get](docs/sdks/refunds/README.md#get) - Get refund

### [transactions](docs/sdks/transactions/README.md)

* [list](docs/sdks/transactions/README.md#list) - List transactions
* [create](docs/sdks/transactions/README.md#create) - Create transaction
* [get](docs/sdks/transactions/README.md#get) - Get transaction
* [capture](docs/sdks/transactions/README.md#capture) - Capture transaction
* [void](docs/sdks/transactions/README.md#void) - Void transaction
* [summary](docs/sdks/transactions/README.md#summary) - Get transaction summary
* [sync](docs/sdks/transactions/README.md#sync) - Sync transaction

#### [transactions.refunds](docs/sdks/transactionsrefunds/README.md)

* [list](docs/sdks/transactionsrefunds/README.md#list) - List transaction refunds
* [create](docs/sdks/transactionsrefunds/README.md#create) - Create transaction refund
* [get](docs/sdks/transactionsrefunds/README.md#get) - Get transaction refund

#### [transactions.refunds.all](docs/sdks/all/README.md)

* [create](docs/sdks/all/README.md#create) - Create batch transaction refund

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Global Parameters [global-parameters] -->
## Global Parameters

A parameter is configured globally. This parameter may be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, This global value will be used as the default on the operations that use it. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `merchant_account_id` to `"default"` at SDK initialization and then you do not have to pass the same value on calls to operations like `get`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


### Available Globals

The following global parameter is available.
Global parameters can also be set via environment variable.

| Name                | Type | Description                                             | Environment               |
| ------------------- | ---- | ------------------------------------------------------- | ------------------------- |
| merchant_account_id | str  | The ID of the merchant account to use for this request. | GR4VY_MERCHANT_ACCOUNT_ID |

### Example

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.merchant_accounts.get(merchant_account_id="merchant-12345")

    # Handle response
    print(res)

```
<!-- End Global Parameters [global-parameters] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.buyers.list(cursor="ZXhhbXBsZTE", search="John", external_identifier="buyer-12345", merchant_account_id="default")

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from gr4vy import Gr4vy
from gr4vy.utils import BackoffStrategy, RetryConfig
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:

    res = g_client.account_updater.jobs.create(payment_method_ids=[
        "ef9496d8-53a5-4aad-8ca2-00eb68334389",
        "f29e886e-93cc-4714-b4a3-12b7a718e595",
    ], merchant_account_id="default",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from gr4vy import Gr4vy
from gr4vy.utils import BackoffStrategy, RetryConfig
import os


with Gr4vy(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
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
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_async` method may raise the following exceptions:

| Error Type                 | Status Code | Content Type     |
| -------------------------- | ----------- | ---------------- |
| errors.Error400            | 400         | application/json |
| errors.Error401            | 401         | application/json |
| errors.Error403            | 403         | application/json |
| errors.Error403Forbidden   | 403         | application/json |
| errors.Error403Active      | 403         | application/json |
| errors.Error404            | 404         | application/json |
| errors.Error405            | 405         | application/json |
| errors.Error409            | 409         | application/json |
| errors.HTTPValidationError | 422         | application/json |
| errors.Error425            | 425         | application/json |
| errors.Error429            | 429         | application/json |
| errors.Error500            | 500         | application/json |
| errors.Error502            | 502         | application/json |
| errors.Error504            | 504         | application/json |
| errors.APIError            | 4XX, 5XX    | \*/\*            |

### Example

```python
from .error403 import Error403Data
from .error403active import Error403ActiveData
from .error403forbidden import Error403ForbiddenData
from gr4vy import Gr4vy, errors
import os


with Gr4vy(
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    merchant_account_id="default",
) as g_client:
    res = None
    try:

        res = g_client.account_updater.jobs.create(payment_method_ids=[
            "ef9496d8-53a5-4aad-8ca2-00eb68334389",
            "f29e886e-93cc-4714-b4a3-12b7a718e595",
        ], merchant_account_id="default")

        assert res is not None

        # Handle response
        print(res)

    except errors.Error400 as e:
        # handle e.data: errors.Error400Data
        raise(e)
    except errors.Error401 as e:
        # handle e.data: errors.Error401Data
        raise(e)
    except errors.Response403CreateAccountUpdaterJob as e:
        if isinstance(e.data, Error403Data):
            # handle custom error data
        elif isinstance(e.data, Error403ForbiddenData):
            # handle custom error data
        elif isinstance(e.data, Error403ActiveData):
            # handle custom error data
        raise(e)
    except errors.Error404 as e:
        # handle e.data: errors.Error404Data
        raise(e)
    except errors.Error405 as e:
        # handle e.data: errors.Error405Data
        raise(e)
    except errors.Error409 as e:
        # handle e.data: errors.Error409Data
        raise(e)
    except errors.HTTPValidationError as e:
        # handle e.data: errors.HTTPValidationErrorData
        raise(e)
    except errors.Error425 as e:
        # handle e.data: errors.Error425Data
        raise(e)
    except errors.Error429 as e:
        # handle e.data: errors.Error429Data
        raise(e)
    except errors.Error500 as e:
        # handle e.data: errors.Error500Data
        raise(e)
    except errors.Error502 as e:
        # handle e.data: errors.Error502Data
        raise(e)
    except errors.Error504 as e:
        # handle e.data: errors.Error504Data
        raise(e)
    except errors.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name         | Server                               | Variables | Description |
| ------------ | ------------------------------------ | --------- | ----------- |
| `production` | `https://api.{id}.gr4vy.app`         | `id`      |             |
| `sandbox`    | `https://api.sandbox.{id}.gr4vy.app` | `id`      |             |

If the selected server has variables, you may override its default values through the additional parameters made available in the SDK constructor:

| Variable | Parameter | Default     | Description                            |
| -------- | --------- | ----------- | -------------------------------------- |
| `id`     | `id: str` | `"example"` | The subdomain for your Gr4vy instance. |

#### Example

```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    server="sandbox",
    id="<id>"
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

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from gr4vy import Gr4vy
import os


with Gr4vy(
    server_url="https://api.example.gr4vy.app",
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from gr4vy import Gr4vy
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Gr4vy(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from gr4vy import Gr4vy
from gr4vy.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Gr4vy(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Gr4vy` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from gr4vy import Gr4vy
import os
def main():

    with Gr4vy(
        bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
        merchant_account_id="default",
    ) as g_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Gr4vy(
        bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
        merchant_account_id="default",
    ) as g_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from gr4vy import Gr4vy
import logging

logging.basicConfig(level=logging.DEBUG)
s = Gr4vy(debug_logger=logging.getLogger("gr4vy"))
```

You can also enable a default debug logger by setting an environment variable `GR4VY_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=gr4vy&utm_campaign=python)
