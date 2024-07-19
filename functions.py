import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt


def get_yahoo_finance_data(ticker_symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Retrieves historical data for the selected stock from Yahoo Finance.

    Args:
        ticker_symbol (str): Ticker symbol of the stock.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pandas.DataFrame: Historical data for the selected stock.
    """
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(start=start_date, end=end_date)
    return data


def plot_timeseries(data: pd.DataFrame, ticker_symbol: str):
    """
    Plots the closing price of the selected stock over time.

    Args:
        data (pandas.DataFrame): Historical data for the selected stock.
        ticker_symbol (str): The ticker symbol of the stock.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'])
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Closing Price (USD)', fontsize=18)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.title(ticker_symbol + ' Stock Price Over Time', fontsize=23)
    plt.show()


def low_pass_filter(data: pd.DataFrame, cutoff_freq: float, sample_rate: float, order: int = 4) -> pd.DataFrame:
    """
    Applies a low-pass filter to the input data.

    Args:
        data (pandas.Series): Input data to be filtered.
        cutoff_freq (float): Cutoff frequency for the low-pass filter.
        sample_rate (float): Sampling rate of the input data.
        order (int): Order of the Butterworth filter (default is 4).

    Returns:
        pandas.Series: Filtered data.
    """
    nyquist_freq = sample_rate / 2
    normalized_cutoff = cutoff_freq / nyquist_freq
    b, a = butter(order, normalized_cutoff, btype='low', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data


def plot_filtered_timeseries(data: pd.DataFrame, filtered_close_prices: pd.DataFrame, ticker_symbol: str):
    """
    Plots the closing price of the selected stock over time after applying a low-pass filter.

    Args:
        data (pandas.DataFrame): Historical data for the selected stock.
        filtered_close_prices (pandas.DataFrame): Filtered close prices for the selected stock.
        ticker_symbol (str): The ticker symbol of the stock.
    """
    plt.figure(figsize=(12, 6))

    data_ = data
    filtered_close_prices_ = filtered_close_prices

    plt.plot(data_.index, filtered_close_prices_)
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Closing Price (USD)', fontsize=18)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.title(ticker_symbol + ' Stock Price Over Time (Filtered)', fontsize=23)
    plt.show()


def plot_3d_phase_space(close_prices: pd.DataFrame, time_delay_parameter: int, ticker_symbol: str):
    """
    Plots the closing price of the selected stock according to the axes y(t), y(t-5), and y(t-10).

    Args:
        close_prices (pandas.DataFrame): Close prices for the selected stock.
        time_delay_parameter (int): Time delay parameter of the phase space reconstruction.
        ticker_symbol (str): The ticker symbol of the stock.
    """
    plt.figure(figsize=(8, 8))
    ax = plt.axes(projection='3d')

    close_prices_ = close_prices
    ax.scatter3D(close_prices_[2*time_delay_parameter:],
                 close_prices_[time_delay_parameter:-time_delay_parameter],
                 close_prices_[:-2*time_delay_parameter],
                 c=close_prices_[:-2*time_delay_parameter],
                 cmap='viridis')

    ax.set_xlabel('y(t)', fontsize=18)
    ax.set_ylabel('y(t-' + str(time_delay_parameter) + ')', fontsize=18)
    ax.set_zlabel('y(t-' + str(2*time_delay_parameter) + ')', fontsize=18)
    ax.set_title(ticker_symbol + ' Stock Price:\n Reconstructed Phase Space', fontsize=21)
    plt.show()


def plot_3d_phase_space_of_filtered_data(filtered_close_prices: pd.DataFrame,
                                         time_delay_parameter: int,
                                         ticker_symbol: str):
    """
    Plots the closing price of the selected stock according to the axes y(t), y(t-5), and y(t-10) after applying a low-pass filter.

    Args:
        filtered_close_prices (pandas.DataFrame): Filtered close prices for the selected stock.
        time_delay_parameter (int): Time delay parameter of the phase space reconstruction.
        ticker_symbol (str): The ticker symbol of the stock.
    """
    plt.figure(figsize=(8, 8))
    ax = plt.axes(projection='3d')

    filtered_close_prices_ = filtered_close_prices

    ax.scatter3D(filtered_close_prices_[2*time_delay_parameter:],
                 filtered_close_prices_[time_delay_parameter:-time_delay_parameter],
                 filtered_close_prices_[:-2*time_delay_parameter],
                 c=filtered_close_prices_[:-2*time_delay_parameter],
                 cmap='viridis')

    ax.set_xlabel('y(t)', fontsize=18)
    ax.set_ylabel('y(t-' + str(time_delay_parameter) + ')', fontsize=18)
    ax.set_zlabel('y(t-' + str(2*time_delay_parameter) + ')', fontsize=18)
    ax.set_title(ticker_symbol + ' Stock Price (Filtered):\n Reconstructed Phase Space', fontsize=21)
    plt.show()
