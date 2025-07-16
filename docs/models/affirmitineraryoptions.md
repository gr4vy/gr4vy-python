# AffirmItineraryOptions


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `type`                                           | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The type of itinerary object.                    | flight                                           |
| `sku`                                            | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The booking/itinerary number (if applicable).    | ABC123                                           |
| `display_name`                                   | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | Readable description of the itinerary item.      | MIA-DCA-2019-12-11T12:07                         |
| `venue`                                          | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The name of the venue where the event is hosted. | Petco Park                                       |
| `location`                                       | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The address object that can be parsed.           | 925 Collins Avenue, Miami Beach, FL, 33140, US   |
| `date_start`                                     | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The start date of this itinerary item.           | 2019-12-05                                       |
| `management`                                     | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The corporation.                                 | Marriott                                         |