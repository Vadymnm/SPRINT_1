import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    """
    function downloads  data of given ticker
    for given period  and  return DataFrame.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
    function calculate average price of "Closed" data  by
    moving  window  with given size  and  store  results
    to the new added  column of DataFrame.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
    function calculate average price of "Closed" data.
    Result is printed out in console.
    """
    x = data['Close'].mean()
    print('--------------------------------------------------')
    print('Average closed price for period  is:', round(x, 3))
    print('--------------------------------------------------')
    return x


def notify_if_strong_fluctuations(data, threshold):
    """
    function get DataFrame(data),  calculate minimum  and maximum
    price, and compare ratio of minimum  and maximum  with
    given threshold. Result is printed out in console.
    """
    min_ = data['Low'].min()
    max_ = data['High'].max()
    print('min price = ', round(min_, 3), ';', 'max price = ', round(max_, 3))
    if int(round((max_-min_)/min_, 2)*100) > int(threshold):
        print('Колебания цены за контрольный период БОЛЕЕ', threshold, "%  !!!")
        print('--------------------------------------------------')
    else:
        print('Колебания цены за контрольный период  НЕ БОЛЕЕ', threshold, "%  !!!")


def export_data_to_csv(data, filename):
    """
    function get DataFrame(data) and save
    data as filename file in .csv format
    """
    data.to_csv(filename)
    print(f"DataFrame сохранен как {filename}")
