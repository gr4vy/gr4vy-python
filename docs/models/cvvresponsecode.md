# CVVResponseCode

## Example Usage

```python
from gr4vy.models import CVVResponseCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: CVVResponseCode = "match"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"match"`
- `"no_match"`
- `"unavailable"`
- `"not_provided"`
