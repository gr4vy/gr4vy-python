# TransactionPaymentSource

The way payment method information made it to this transaction.

## Example Usage

```python
from gr4vy.models import TransactionPaymentSource

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TransactionPaymentSource = "ecommerce"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"ecommerce"`
- `"moto"`
- `"recurring"`
- `"installment"`
- `"card_on_file"`
