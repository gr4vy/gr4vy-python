# ReportExecutionStatus

## Example Usage

```python
from gr4vy.models import ReportExecutionStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ReportExecutionStatus = "dispatched"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"dispatched"`
- `"failed"`
- `"pending"`
- `"processing"`
- `"succeeded"`
