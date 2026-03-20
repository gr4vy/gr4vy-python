# Flow

## Example Usage

```python
from gr4vy.models import Flow

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Flow = "checkout"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"checkout"`
- `"card-transaction"`
- `"non-card-transaction"`
- `"redirect-transaction"`
