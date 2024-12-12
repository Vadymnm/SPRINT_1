import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['High'].values, label='High')
            plt.plot(dates, data['Low'].values, label='Low')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def create_and_save_rsi_plot(data, ticker, period, rsi, filename=None):
    """
    function get DataFrame(data),  ticker, period of analyze, rsi table
    and  filename (optional) and create two charts  with "Close" data
    and RSI  at  the  same page.  Page image is saved in .png file.
    """

    """  Create new list  for picture. """
    plt.figure(figsize=(10, 6))
    """  Create two charts on the same figure."""
    ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
    ax2 = plt.subplot2grid((10, 1), (6, 0), rowspan=4, colspan=1)

    """  First chart:
        Plot the closing price on the first chart """
    ax1.plot(data['Close'], linewidth=2)
    ax1.set_title(f"{ticker}, Close price")

    """  Second chart
         Plot the RSI  """
    ax2.set_title('Relative Strength Index')
    ax2.plot(rsi, color='orange', linewidth=1)
    """ Add two horizontal lines, signalling the buy and sell ranges. """
    """ Oversold """
    ax2.axhline(30, linestyle='--', linewidth=1.5, color='green')
    """  Overbought """
    ax2.axhline(70, linestyle='--', linewidth=1.5, color='red')

    """  Save  charts  to  file """
    if filename is None:
        filename = f"{ticker}_{period}_RSI_chart.png"
    plt.savefig(filename)
    print(f"График сохранен как {filename}")

    """ Display the charts """
    plt.show()
