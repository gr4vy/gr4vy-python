# CreateReportExecutionURLRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `report_id`                                                | *str*                                                      | :heavy_check_mark:                                         | The ID of the report to retrieve a URL for.                | 4d4c7123-b794-4fad-b1b9-5ab2606e6bbe                       |
| `report_execution_id`                                      | *str*                                                      | :heavy_check_mark:                                         | The ID of the execution of a report to retrieve a URL for. | 003bc416-f32a-420c-8eb2-062a386e1fb0                       |
| `merchant_account_id`                                      | *Optional[str]*                                            | :heavy_minus_sign:                                         | The ID of the merchant account to use for this request.    | default                                                    |