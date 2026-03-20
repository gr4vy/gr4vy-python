# FlowAction

## Example Usage

```python
from gr4vy.models import FlowAction

# Open enum: unrecognized values are captured as UnrecognizedStr
value: FlowAction = "select-payment-options"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"select-payment-options"`
- `"route-transaction"`
- `"decline-early"`
- `"skip-3ds"`
