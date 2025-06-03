# ReportExecutionURL


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `url`                                                                | *str*                                                                | :heavy_check_mark:                                                   | A signed URL to download the report execution file.                  | https://example.com/download/report.csv?signature=abc123             |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The date and time when the download URL expires.                     | 2024-06-01T00:00:00.000Z                                             |