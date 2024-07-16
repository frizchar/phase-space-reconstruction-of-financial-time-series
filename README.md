# Phase space reconstruction of financial data
### Overview
We process historical data of stocks following the steps below:
1. pull historical data of the selected stock using the [yfinance](https://pypi.org/project/yfinance/) package (_in our implementation we select the Apple stock_)
1. apply a low-pass Butterworth filter on the stock data
1. plot the stock time-series
1. plot the reconstructed phase space of the time-series as in Doyne Farmer's famous paper [Geometry from a Time Series](https://www.datascienceassn.org/sites/default/files/Geometry%20from%20a%20Time%20Series.pdf)<br>
In this case, regarding the embedding dimension $d$ we choose $d = 3$

### Input parameters
-  __ticker_symbol__ (_string_):= ticker symbol of selected stock
-  __start_date__ (_string_):= start date of historical data in 'YYYY-MM-DD' format
-  __end_date__ (_string_):= end date of historical data in 'YYYY-MM-DD' format
-  __cutoff_freq__ (_float_):= cutoff frequency for the low-pass filter
-  __sample_rate__ (_float_):= sampling rate of the input data used for the low-pass filter
-  __order__ (_int_):= order of the Butterworth low-pass filter
-  __time_delay_parameter__ (_int_):= time delay parameter of the phase space embedding

### Dependencies
The required packages are included in file ```requirements.txt```.<br>
Python interpreter version used for this project: **3.9.4**

