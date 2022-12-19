from typing import *

import pandas as pd
import os
import matplotlib.pyplot as plt

tickers = {file_name: pd.read_csv("EastSpringData/" + file_name) for file_name in os.listdir("EastSpringData/")}
curr_data_frame = tickers["000660.KS.csv"]
curr_data_frame.index = pd.to_datetime(curr_data_frame.index)
print(curr_data_frame.index)
print("above this")
print(curr_data_frame.columns)
print(curr_data_frame.head(2))

def returns_for_stock(ticker_name):
    curr_df = tickers[ticker_name]
    curr_returns = curr_df["Adj Close"].pct_change()
    curr_returns = curr_returns.dropna()

    return curr_returns

curr_returns = returns_for_stock("000660.KS.csv")
mean = curr_returns.mean()
median = curr_returns.median()
std = curr_returns.std()
skew = curr_returns.skew()
kurtosis = curr_returns.kurtosis()

print("Mean:", mean)
print("Median:", median)
print("Standard deviation:", std)
print("Skew:", skew)
print("Kurtosis:", kurtosis)

plt.interactive(False)
print(curr_returns.hist())
print(curr_returns.plot.density())
print('===============================')
print("IS MONTH FROM HERE ON")
print("=====================================")
# Select month-end prices

curr_data_frame.index = pd.to_datetime(curr_data_frame.index)
curr_data_frame['Date'] = pd.to_datetime(curr_data_frame['Date'])
month_end_prices = curr_data_frame.groupby(pd.Grouper(key="Date", freq="M")).last()
curr_monthly_returns = month_end_prices["Adj Close"].pct_change()
curr_monthly_returns.dropna(inplace=True)

month_mean = curr_monthly_returns.mean()
month_median = curr_monthly_returns.median()
month_std = curr_monthly_returns.std()
month_skew = curr_monthly_returns.skew()
month_kurtosis = curr_monthly_returns.kurtosis()

print("Monthly Mean:", month_mean)
print("Monthly Median:", month_median)
print("Monthly Standard deviation:", month_std)
print("Month Skew:", month_skew)
print("Month Kurtosis:", month_kurtosis)

print(curr_monthly_returns.hist())

print(curr_returns)
print('===============================')
print(curr_monthly_returns)


# curr_monthly_returns.describe()