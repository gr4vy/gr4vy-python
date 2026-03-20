# ThreeDSecureStatus

## Example Usage

```python
from gr4vy.models import ThreeDSecureStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ThreeDSecureStatus = "setup_error"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"setup_error"`
- `"error"`
- `"declined"`
- `"cancelled"`
- `"complete"`
