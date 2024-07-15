import functions

# Input parameters: stock
ticker_symbol = "AAPL"
start_date = "2020-01-01"
end_date = "2023-12-31"
data = functions.get_yahoo_finance_data(ticker_symbol, start_date, end_date)
print(data.head())


if __name__ == '__main__':
    functions.plot_stock(data)
    functions.plot_filtered_data(data)
    functions.plot_3d__phase_space(data)
    functions.plot_3d_phase_space_of_filtered_data(data)
