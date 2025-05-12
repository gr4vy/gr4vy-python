# AuditLogEntryUser


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `type`                                       | *Optional[Literal["user"]]*                  | :heavy_minus_sign:                           | Always `user`.                               | user                                         |
| `id`                                         | *OptionalNullable[str]*                      | :heavy_minus_sign:                           | The ID of the user.                          | 14b7b8c5-a6ba-4fb6-bbab-52d43c7f37ef         |
| `name`                                       | *str*                                        | :heavy_check_mark:                           | The name of the user.                        | John Doe                                     |
| `email_address`                              | *OptionalNullable[str]*                      | :heavy_minus_sign:                           | The email address for this user.             | john@example.com                             |
| `is_staff`                                   | *bool*                                       | :heavy_check_mark:                           | Whether this is a Gr4vy staff user.          | false                                        |
| `status`                                     | [models.UserStatus](../models/userstatus.md) | :heavy_check_mark:                           | N/A                                          |                                              |