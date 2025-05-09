# ListMerchantAccountsRequest


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       | Example                                           |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `cursor`                                          | *OptionalNullable[str]*                           | :heavy_minus_sign:                                | A pointer to the page of results to return.       | ZXhhbXBsZTE                                       |
| `limit`                                           | *Optional[int]*                                   | :heavy_minus_sign:                                | The maximum number of items that are at returned. | 20                                                |
| `search`                                          | *OptionalNullable[str]*                           | :heavy_minus_sign:                                | The search term to filter merchant accounts by.   | merchant-12345                                    |