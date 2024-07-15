import functions

# Input parameters: ticker_symbol, start_date, end_date
ticker_symbol = "AAPL"
# input dates in 'YYYY-MM-DD' format
start_date = "2020-01-01"
end_date = "2023-12-31"
data = functions.get_yahoo_finance_data(ticker_symbol, start_date, end_date)
print(data.head())


if __name__ == '__main__':
    functions.plot_timeseries(data)
    functions.plot_filtered_data(data)
    functions.plot_3d_phase_space(data)
    functions.plot_3d_phase_space_of_filtered_data(data)
