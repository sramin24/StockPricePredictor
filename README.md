
# StockPricePredictor

One-feature linear regression stock-price forecasting in Python.

## Requirements

- Python 3.6+  
- Install dependencies:
  ```bash
  pip install yfinance pandas scikit-learn matplotlib

## Usage

1. Configure at the top of `stock_price_predictor_horizon.py`:

   ```python
   ticker = "AAPL"         # e.g. "MSFT", "GOOG"
   start_date = "2020-01-01"
   end_date = "2025-05-12"
   forecast_months = 1      # months ahead
   forecast_years = 0       # years ahead
   ```
2. Run:

   ```bash
   python stock_price_predictor_horizon.py
   ```

## Description

* Downloads historical closing prices via `yfinance`
* Trains a Linear Regression on yesterday’s close → today’s close
* Iteratively forecasts your chosen horizon (months/years) business day by business day

## Example Output

```
Predicted close for AAPL on 2025-06-12: $178.42
```

## Future Improvements

* Add technical indicators (moving averages, volume)
* Use time-series models (ARIMA, Prophet, LSTM)
* Batch-forecast multiple horizons and plot results

## License

MIT

```
```
