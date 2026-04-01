#!/usr/bin/env python

import yfinance as yf
import matplotlib.pyplot as plt
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker", nargs="+", help="Stock ticker(s)")
    time_range = parser.add_mutually_exclusive_group()
    time_range.add_argument("-y", "--ytd", action="store_true", help="Period: year-to-date (default)")
    time_range.add_argument("-Y", "--year", action="store_true", help="Period: one year")
    time_range.add_argument("-w", "--week", action="store_true", help="Period: one week")
    time_range.add_argument("-m", "--month", action="store_true", help="Period: one month")
    time_range.add_argument("-5", "--five-year", action="store_true", help="Period: five years")
    time_range.add_argument("-10", "--ten-year", action="store_true", help="Period: ten years")
    time_range.add_argument("-M", "--max", action="store_true", help="Period: Maximum")
    args = parser.parse_args()

    # Default period to be for year-to-date
    period = "ytd"

    if args.year:
        period = "1y"
    elif args.week:
        period = "5d"
    elif args.month:
        period = "1mo"
    elif args.five_year:
        period = "5y"
    elif args.ten_year:
        period = "10y"
    elif args.max:
        period = "max"

    tickers = set([ticker.upper() for ticker in args.ticker])
    tickers_queried = []
    plt.style.use("dark_background")
    plt.figure(figsize=(10, 5))
    plt.xlabel("Date")
    plt.ylabel("Cumulative return (%)")

    for ticker in tickers:
        data = yf.download(ticker, period=period)

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
