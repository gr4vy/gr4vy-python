# RefundStatus

## Example Usage

```python
from gr4vy.models import RefundStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RefundStatus = "processing"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"processing"`
- `"succeeded"`
- `"failed"`
- `"declined"`
- `"voided"`
