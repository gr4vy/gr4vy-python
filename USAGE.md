<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from gr4vy import Gr4vy
import os


with Gr4vy(
    merchant_account_id="default",
    bearer_auth=os.getenv("GR4VY_BEARER_AUTH", ""),
) as g_client:

    res = g_client.browse_payment_method_definitions_get()

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

        res = await g_client.browse_payment_method_definitions_get_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->