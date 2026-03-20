# ErrorLocation

## Example Usage

```python
from gr4vy.models import ErrorLocation

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ErrorLocation = "query"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"query"`
- `"body"`
- `"path"`
- `"header"`
- `"unknown"`
