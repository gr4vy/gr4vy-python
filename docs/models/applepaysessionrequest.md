# ApplePaySessionRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `validation_url`                                                           | *str*                                                                      | :heavy_check_mark:                                                         | The validation URL as provided by the Apple SDK when processing a payment. | https://apple-pay-gateway-cert.apple.com                                   |
| `domain_name`                                                              | *str*                                                                      | :heavy_check_mark:                                                         | The domain on which Apple Pay is being loaded.                             | example.com                                                                |