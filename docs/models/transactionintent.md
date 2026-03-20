# TransactionIntent

## Example Usage

```python
from gr4vy.models import TransactionIntent

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TransactionIntent = "authorize"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"authorize"`
- `"capture"`
