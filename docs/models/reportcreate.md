# ReportCreate


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `name`                                               | *str*                                                | :heavy_check_mark:                                   | The name of the report.                              | Monthly Transaction Report                           |
| `description`                                        | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | A description of the report.                         | Monthly transaction summary for May 2024.            |
| `schedule`                                           | [models.ReportSchedule](../models/reportschedule.md) | :heavy_check_mark:                                   | N/A                                                  |                                                      |
| `schedule_enabled`                                   | *bool*                                               | :heavy_check_mark:                                   | Whether the report schedule is enabled.              | true                                                 |
| `schedule_timezone`                                  | *Optional[str]*                                      | :heavy_minus_sign:                                   | The timezone for the report schedule.                | UTC                                                  |
| `spec`                                               | [models.Spec](../models/spec.md)                     | :heavy_check_mark:                                   | The report specification.                            |                                                      |