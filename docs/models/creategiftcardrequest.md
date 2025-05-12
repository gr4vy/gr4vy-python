# CreateGiftCardRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `timeout_in_seconds`                                    | *Optional[float]*                                       | :heavy_minus_sign:                                      | N/A                                                     |                                                         |
| `merchant_account_id`                                   | *Optional[str]*                                         | :heavy_minus_sign:                                      | The ID of the merchant account to use for this request. | default                                                 |
| `gift_card_create`                                      | [models.GiftCardCreate](../models/giftcardcreate.md)    | :heavy_check_mark:                                      | N/A                                                     |                                                         |