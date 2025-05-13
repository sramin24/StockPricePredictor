````markdown
# StockPricePredictor

One‐feature linear regression stock‐price forecasting in Python.

## Requirements

- Python 3.6+  
- pip packages:
  ```bash
  pip install yfinance pandas scikit-learn matplotlib
````

## Usage

1. Edit the configuration at the top of `stock_price_predictor_horizon.py`:

   ```python
   ticker         = "AAPL"       # e.g. "MSFT", "GOOG", etc.
   start_date     = "2020-01-01" # historical data start
   end_date       = "2025-05-12" # historical data end
   forecast_months = 1           # months ahead to predict
   forecast_years  = 0           # years ahead to predict
   ```
2. Run the script:

   ```bash
   python stock_price_predictor_horizon.py
   ```
3. See the printed “Predicted close for …” line in your console.

## What it does

* Downloads historical daily closing prices via `yfinance`
* Trains a linear regression on “yesterday’s close → today’s close”
* Iteratively forecasts your chosen horizon (in months/years), stepping business day by business day

## Example Output

```
Predicted close for AAPL on 2025-06-12: $178.42
```

## Future Improvements

* Add technical indicators (moving averages, volume, volatility)
* Swap to time‐series models (ARIMA, Prophet, LSTM) for better long‐term forecasts
* Batch‐forecast multiple horizons and visualize results

## License

This project is licensed under the MIT License.

```
```
