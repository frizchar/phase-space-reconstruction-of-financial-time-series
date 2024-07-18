# Phase space reconstruction of financial data
### Overview
In this project we attempt to reconstruct the phase space of the ```AAPL``` stock.<br>
Specifically, we follow the steps below:
1. pull historical data of the selected stock using the [yfinance](https://pypi.org/project/yfinance/) package
1. apply a low-pass Butterworth filter on the data, in order to explore the low-frequency signal
1. plot the stock time-series
1. plot the reconstructed phase space of the time-series as in Doyne Farmer's famous paper [Geometry from a Time Series](https://www.datascienceassn.org/sites/default/files/Geometry%20from%20a%20Time%20Series.pdf)<br>
Namely, any time series $x_i$ may be restructured as $d$-dimensional vectors of the form $(^1x_i, ^2x_{i+\tau}, ..., ^dx_{i+(d-1)\cdot\tau})$,<br>
where $d$ is the embedding dimension of the phase space and $\tau$ is the time delay parameter.<br>
In our example we plot the $3$-dimensional phase space, hence $d = 3$

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

