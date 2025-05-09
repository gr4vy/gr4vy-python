<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from gr4vy import Gr4vy
import os


with Gr4vy(
    server="sandbox",
    id="example",
    bearer_auth=auth.with_token(open("./private_key.pem").read(), expires_in=1),
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from gr4vy import Gr4vy
import os

async def main():

    async with Gr4vy(
        server="sandbox",
    id="example",
    bearer_auth=auth.with_token(open("./private_key.pem").read(), expires_in=1),
        merchant_account_id="default",
    ) as g_client:

        res = await g_client.account_updater.jobs.create_async(payment_method_ids=[
            "ef9496d8-53a5-4aad-8ca2-00eb68334389",
            "f29e886e-93cc-4714-b4a3-12b7a718e595",
        ], merchant_account_id="default")

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->