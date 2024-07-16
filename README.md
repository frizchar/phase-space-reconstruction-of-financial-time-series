# Phase space reconstruction of financial data
### Overview
We process historical data of stocks following the steps below:
1. pull historical data of the selected stock using the [yfinance](https://pypi.org/project/yfinance/) package (_in our implementation we select the Apple stock_)
1. apply low-pass Butterworth filtering on the stock data
1. plot both initial and filtered stock time-series
1. plot reconstructed phase space as in Doyne Farmer's famous paper [Geometry from a Time Series](https://www.datascienceassn.org/sites/default/files/Geometry%20from%20a%20Time%20Series.pdf)<br>
In our case we choose<br>
   - embedding dimension $d = 3$ and
   - time delay $\tau = 5$

### Input parameters
-  __ticker_symbol__ (_string_):= ticker symbol of selected stock
-  __start_date__ (_string_):= start date of historical data in 'YYYY-MM-DD' format
-  __end_date__ (_string_):= end date of historical data in 'YYYY-MM-DD' format
-  __cutoff_freq__ (_float_):= cutoff frequency for the low-pass filter
-  __sample_rate__ (_float_):= sampling rate of the input data
-  __order__ (_int_):= order of the Butterworth filter

### Dependencies
The required packages are included in file ```requirements.txt```.<br>
Python interpreter version used for this project: **3.9.4**

