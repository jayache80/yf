# yf.py

Query Yahoo Finance data and plot overlays of stock ticker cumulative returns.

    usage: yf.py [-h] [-y | -Y | -w | -m | -5 | -10 | -M] ticker [ticker ...]

    positional arguments:
      ticker           Stock ticker(s)

    options:
      -h, --help       show this help message and exit
      -y, --ytd        Period: year-to-date (default)
      -Y, --year       Period: one year
      -w, --week       Period: one week
      -m, --month      Period: one month
      -5, --five-year  Period: five years
      -10, --ten-year  Period: ten years
      -M, --max        Period: Maximum

Example:

    ./yf.py aapl amd

![](example.png)
