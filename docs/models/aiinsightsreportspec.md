# AIInsightsReportSpec


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `model`                                                | *Optional[Literal["ai_insights"]]*                     | :heavy_minus_sign:                                     | The report model type.                                 | ai_insights                                            |
| `params`                                               | Dict[str, *Any*]                                       | :heavy_check_mark:                                     | The parameters for the AI insights report model.       | {<br/>"filters": {<br/>"prompt_key": "payment_performance"<br/>}<br/>} |