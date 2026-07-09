# Interval

The cadence unit for the subscription plan.

## Example Usage

```python
from gr4vy.models import Interval

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Interval = "DAY"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"DAY"`
- `"WEEK"`
- `"MONTH"`
- `"YEAR"`
