# AuditLogAction

## Example Usage

```python
from gr4vy.models import AuditLogAction

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AuditLogAction = "created"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"created"`
- `"updated"`
- `"deleted"`
- `"voided"`
- `"canceled"`
- `"captured"`
