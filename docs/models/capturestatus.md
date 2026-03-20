# CaptureStatus

## Example Usage

```python
from gr4vy.models import CaptureStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: CaptureStatus = "succeeded"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"succeeded"`
- `"pending"`
- `"declined"`
- `"failed"`
