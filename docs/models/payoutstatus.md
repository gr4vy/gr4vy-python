# PayoutStatus

## Example Usage

```python
from gr4vy.models import PayoutStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PayoutStatus = "declined"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"declined"`
- `"failed"`
- `"pending"`
- `"succeeded"`
