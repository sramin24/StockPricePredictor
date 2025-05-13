# stock_price_predictor_horizon_fixed.py

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from pandas.tseries.offsets import BDay, DateOffset

def fetch_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    df = df[['Close']]
    df['Prev_Close'] = df['Close'].shift(1)
    df.dropna(inplace=True)
    return df

def train_on_all(data):
    X = data[['Prev_Close']]
    y = data['Close']
    return LinearRegression().fit(X, y)

def forecast_horizon(model, last_close, last_date, months=0, years=0):
    """
    Advance one business day at a time until last_date + (months, years),
    always passing a pure Python float into model.predict, and extracting
    the scalar via .item().
    """
    target = last_date + DateOffset(months=months, years=years)
    current_close = last_close       # already a Python float
    current_date  = last_date

    while current_date < target:
        current_date += BDay(1)
        # prepare a (1,1) array
        X_input = np.array([[current_close]])
        # predict returns a 1-element array; extract via [0].item()
        pred = model.predict(X_input)[0].item()
        current_close = pred

    return current_date.date(), current_close

if __name__ == "__main__":
    ticker         = "AAPL"
    start_date     = "2020-01-01"
    end_date       = "2025-05-12"
    forecast_months = 1
    forecast_years  = 0

    # 1) Fetch & train
    data       = fetch_data(ticker, start_date, end_date)
    model_full = train_on_all(data)

    # 2) Grab last_close as a Python float (not a Series!)
    last_close = data['Close'].iloc[-1].item()
    last_date  = data.index[-1]

    # 3) Forecast
    target_date, target_pred = forecast_horizon(
        model_full, last_close, last_date,
        months=forecast_months,
        years=forecast_years
    )

    print(f"Predicted close for {ticker} on {target_date}: ${target_pred:.2f}")
