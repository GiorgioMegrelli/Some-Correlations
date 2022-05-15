from datetime import datetime

import pandas as pd
import yfinance as yf

YF_DAY = "1d"
COLUMNS_IN_AVG = ["Open", "High", "Low", "Close"]
COLUMN_VOLUME = "Volume"
COLUMN_AVG = "OHLC-Avg"


def download_range(
    ticker_name: str, start: str | datetime, end: str | datetime, interval: str
) -> pd.DataFrame:
    tk = yf.Ticker(ticker_name)
    return tk.history(start=start, end=end, interval=interval, actions=False)


def download_daily_avg(
    ticker_name: str, start: str | datetime, end: str | datetime, del_cols: bool = True
) -> pd.DataFrame:
    data = download_range(ticker_name, start, end, YF_DAY)
    del data[COLUMN_VOLUME]
    data[f"{COLUMN_AVG} {ticker_name}"] = data.mean(axis=1)
    if del_cols:
        for col in COLUMNS_IN_AVG:
            del data[col]
    return data
