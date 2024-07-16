import functions


# INPUT PARAMETERS
###########################
ticker_symbol = "AAPL"      # Ticker symbol of selected stock
start_date = "2020-01-01"   # Start date of historical data in 'YYYY-MM-DD' format
end_date = "2023-12-31"     # End date of historical data in 'YYYY-MM-DD' format
cutoff_freq = 0.01          # Cutoff frequency for the low-pass filter
sample_rate = 1             # Sampling rate of the input data
order = 4                   # Order of the Butterworth filter
time_delay_parameter = 25    # Time delay parameter of phase space embedding
###########################


if __name__ == '__main__':
    data = functions.get_yahoo_finance_data(ticker_symbol, start_date, end_date)
    close_prices = data['Close']
    filtered_close_prices = functions.low_pass_filter(close_prices, cutoff_freq, sample_rate, order)
    print(data.head())

    functions.plot_timeseries(data)
    functions.plot_filtered_timeseries(data, filtered_close_prices)
    functions.plot_3d_phase_space(close_prices, time_delay_parameter)
    functions.plot_3d_phase_space_of_filtered_data(filtered_close_prices, time_delay_parameter)
