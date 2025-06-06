<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.account_updater.jobs.create(payment_method_ids=[
        "ef9496d8-53a5-4aad-8ca2-00eb68334389",
        "f29e886e-93cc-4714-b4a3-12b7a718e595",
    ])

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
        merchant_account_id="default",
        bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
    ) as g_client:

        res = await g_client.account_updater.jobs.create_async(payment_method_ids=[
            "ef9496d8-53a5-4aad-8ca2-00eb68334389",
            "f29e886e-93cc-4714-b4a3-12b7a718e595",
        ])

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->