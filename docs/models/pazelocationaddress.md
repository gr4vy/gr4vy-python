# PazeLocationAddress


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `name`                                             | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | Name of the organization or entity at the address. |
| `line1`                                            | *str*                                              | :heavy_check_mark:                                 | Line 1 of the address.                             |
| `line2`                                            | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | Line 2 of the address.                             |
| `line3`                                            | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | Line 3 of the address.                             |
| `city`                                             | *str*                                              | :heavy_check_mark:                                 | City.                                              |
| `state`                                            | *str*                                              | :heavy_check_mark:                                 | State or region.                                   |
| `zip`                                              | *str*                                              | :heavy_check_mark:                                 | Postal code.                                       |
| `country_code`                                     | *str*                                              | :heavy_check_mark:                                 | ISO 3166-1 alpha-2 country code.                   |