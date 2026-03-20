# AVSResponseCode

## Example Usage

```python
from gr4vy.models import AVSResponseCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AVSResponseCode = "match"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"match"`
- `"no_match"`
- `"partial_match_address"`
- `"partial_match_postcode"`
- `"partial_match_name"`
- `"unavailable"`
