import yfinance as yf
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt


def get_yahoo_finance_data(ticker_symbol:str, start_date: str, end_date: str):
    """
    Retrieves historical ata for the selected stock from Yahoo Finance.

    Args:
        ticker_symbol (str): Ticker symbol of the stock
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pandas.DataFrame: Historical data for the selected stock
    """
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(start=start_date, end=end_date)
    return data


def plot_aapl_stock(data):
    """
    Plots the closing price of the selected stock over time.

    Args:
        data (pandas.DataFrame): Historical data for the selected stock.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Stock Price Over Time')
    plt.show()


def low_pass_filter(data, cutoff_freq, sample_rate, order=4):
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


def plot_aapl_filtered(data, cutoff_freq=0.01, sample_rate=1):
    """
    Plots the closing price of the selected stock over time after applying a low-pass filter.

    Args:
        data (pandas.DataFrame): Historical data for the selected stock
        cutoff_freq (float): Cutoff frequency for the low-pass filter (default is 0.01).
        sample_rate (float): Sampling rate of the input data (default is 1).
    """
    plt.figure(figsize=(12, 6))

    close_prices = data['Close']
    filtered_prices = low_pass_filter(close_prices, cutoff_freq=cutoff_freq, sample_rate=sample_rate)

    plt.plot(data.index, filtered_prices)
    plt.xlabel('Date')
    plt.ylabel('Closing Price (Filtered)')
    plt.title('Stock Price Over Time (Filtered)')
    plt.show()


def plot_3d(data):
    """
    Plots the closing price of the selected stock according to the axes y(t), y(t-5), and y(t-10).

    Args:
        data (pandas.DataFrame): Historical data for the selected stock
    """
    plt.figure(figsize=(8, 8))
    ax = plt.axes(projection='3d')

    close_prices = data['Close']
    ax.scatter3D(close_prices[10:], close_prices[5:-5], close_prices[:-10], c=close_prices[:-10], cmap='viridis')

    ax.set_xlabel('y(t)')
    ax.set_ylabel('y(t-5)')
    ax.set_zlabel('y(t-10)')
    ax.set_title('Stock Price: y(t), y(t-5), y(t-10)')

    plt.show()


def plot_3d_filtered(data):
    """
    Plots the closing price of the selected stock according to the axes y(t), y(t-5), and y(t-10) after applying a low-pass filter.

    Args:
        data (pandas.DataFrame): Historical data for the selected stock
    """
    plt.figure(figsize=(8, 8))
    ax = plt.axes(projection='3d')

    close_prices = data['Close']
    filtered_prices = low_pass_filter(close_prices, cutoff_freq=0.01, sample_rate=1)

    ax.scatter3D(filtered_prices[10:], filtered_prices[5:-5], filtered_prices[:-10], c=filtered_prices[:-10],
                 cmap='viridis')

    ax.set_xlabel('y(t)')
    ax.set_ylabel('y(t-5)')
    ax.set_zlabel('y(t-10)')
    ax.set_title('Stock Price (Filtered): y(t), y(t-5), y(t-10)')

    plt.show()
