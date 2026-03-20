# ProductType

## Example Usage

```python
from gr4vy.models import ProductType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ProductType = "physical"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"physical"`
- `"discount"`
- `"shipping_fee"`
- `"sales_tax"`
- `"digital"`
- `"gift_card"`
- `"store_credit"`
- `"surcharge"`
