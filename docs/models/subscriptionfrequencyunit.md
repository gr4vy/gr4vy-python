# SubscriptionFrequencyUnit

Indicates the frequency unit for the subscription. Allowed values are: `DAY`, `WEEK`, `MONTH`, `BI_MONTHLY`, `QUARTER`, `SEMI_ANNUALLY`, `YEAR`, `ONDEMAND`.

## Example Usage

```python
from gr4vy.models import SubscriptionFrequencyUnit

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SubscriptionFrequencyUnit = "MONTH"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"MONTH"`
- `"WEEK"`
- `"BI_MONTHLY"`
- `"ONDEMAND"`
- `"QUARTER"`
- `"YEAR"`
- `"SEMI_ANNUALLY"`
- `"DAY"`
