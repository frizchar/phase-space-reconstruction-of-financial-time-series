import functions

# INPUT PARAMETERS
ticker_symbol  = "AAPL"      # Ticker symbol of selected stock
START_DATE = "2020-01-01"   # Start date of historical data in 'YYYY-MM-DD' format
END_DATE = "2023-12-31"     # End date of historical data in 'YYYY-MM-DD' format
CUTOFF_FREQ = 0.01          # Cutoff frequency for the low-pass filter
SAMPLE_RATE = 1             # Sampling rate of the input data
ORDER = 4                   # Order of the Butterworth filter
TIME_DELAY_PARAMETER = 25   # Time delay parameter of phase space embedding

if __name__ == '__main__':
    data = functions.get_yahoo_finance_data(TICKER_SYMBOL, START_DATE, END_DATE)
    close_prices = data['Close']
    filtered_close_prices = functions.low_pass_filter(close_prices, CUTOFF_FREQ, SAMPLE_RATE, ORDER)
    print(data.head())

    functions.plot_timeseries(data)
    functions.plot_filtered_timeseries(data, filtered_close_prices)
    functions.plot_3d_phase_space(close_prices, TIME_DELAY_PARAMETER)
    functions.plot_3d_phase_space_of_filtered_data(filtered_close_prices, TIME_DELAY_PARAMETER)
