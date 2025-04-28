# CreateAccountUpdaterJobRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `timeout_in_seconds`                                                   | *Optional[float]*                                                      | :heavy_minus_sign:                                                     | N/A                                                                    |
| `merchant_account_id`                                                  | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The ID of the merchant account to use for this request.                |
| `account_updater_job_create`                                           | [models.AccountUpdaterJobCreate](../models/accountupdaterjobcreate.md) | :heavy_check_mark:                                                     | N/A                                                                    |