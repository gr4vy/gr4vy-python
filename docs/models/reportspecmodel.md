# ReportSpecModel

## Example Usage

```python
from gr4vy.models import ReportSpecModel

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ReportSpecModel = "transactions"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"transactions"`
- `"transaction_retries"`
- `"detailed_settlement"`
- `"accounts_receivables"`
