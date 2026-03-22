#!/usr/bin/env python

import yfinance as yf
import matplotlib.pyplot as plt
import sys
import argparse
from datetime import date
from dateutil.relativedelta import relativedelta

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker", nargs="+", help="Stock ticker(s)")
    time_range = parser.add_mutually_exclusive_group()
    time_range.add_argument("-y", "--ytd", action="store_true", help="Time range: year-to-date (default)")
    time_range.add_argument("-Y", "--year", action="store_true", help="Time range: one year")
    time_range.add_argument("-w", "--week", action="store_true", help="Time range: one week")
    time_range.add_argument("-5", "--five-year", action="store_true", help="Time range: five years")
    time_range.add_argument("-10", "--ten-year", action="store_true", help="Time range: ten years")
    args = parser.parse_args()

    today = date.today()
    end = today.strftime("%Y-%m-%d")
    # Default start time to be for year-to-date
    start = today.strftime("%Y-01-01")

    if args.year:
        start = today - relativedelta(years=1)
    elif args.week:
        start = today - relativedelta(weeks=1)
    elif args.five_year:
        start = today - relativedelta(years=5)
    elif args.ten_year:
        start = today - relativedelta(years=10)

    tickers = set([ticker.upper() for ticker in args.ticker])
    tickers_queried = []
    plt.figure(figsize=(10, 5))
    plt.xlabel("Date")
    plt.ylabel("Cumulative return (%)")

    for ticker in tickers:
        data = yf.download(ticker, start=start, end=end)

        if data.empty:
            print(f"Error downloading {ticker} data. Skipping...")
            continue

        tickers_queried.append(ticker)
        cumulative_returns = (data["Close"] / data["Close"].iloc[0] - 1) * 100
        plt.plot(cumulative_returns, label=ticker)

    if not tickers_queried:
        print("Nothing to plot.")
        return 1

    tickers = ", ".join(tickers_queried)
    plt.title(f"{tickers} Cumulative Returns")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    sys.exit(main())
