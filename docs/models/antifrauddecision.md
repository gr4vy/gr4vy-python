# AntiFraudDecision

## Example Usage

```python
from gr4vy.models import AntiFraudDecision

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AntiFraudDecision = "accept"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"accept"`
- `"error"`
- `"exception"`
- `"reject"`
- `"review"`
- `"skipped"`
- `"pending"`
