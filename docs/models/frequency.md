# Frequency

Indicates the frequency unit for the subscription. Allowed values are: `WEEKLY`, `MONTHLY`, `QUARTERLY`, `SEMI_ANNUAL`, `ANNUAL`.

## Example Usage

```python
from gr4vy.models import Frequency

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Frequency = "WEEKLY"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"WEEKLY"`
- `"MONTHLY"`
- `"QUARTERLY"`
- `"SEMI_ANNUAL"`
- `"ANNUAL"`
