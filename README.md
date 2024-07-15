# Phase space of filtered stock data
### Overview
We applie low-pass filtering on historical data of stocks, following the steps below:<br>
1. pull historical data of the selected stock using the [yfinance](https://pypi.org/project/yfinance/) package
1. apply low-pass Butterworth filtering on the stock data
1. plot both initial and filtered stock data
1. plot reconstructed phase space as in Doyne Farmer's famous [paper](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.45.712)

### Dependencies
The required packages are included in file ```requirements.txt```.<br>
Python interpreter version used for this project: **3.9.4**

