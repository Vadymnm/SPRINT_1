import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    x = data['Close'].mean()
    print('--------------------------------------------------')
    print('Average closed price for period  is:', round(x, 3))
    print('--------------------------------------------------')
    return x


def notify_if_strong_fluctuations(data, threshold):
    min_ = data['Low'].min()
    max_ = data['High'].max()
    print('min price = ', round(min_, 3), ';', 'max price = ', round(max_, 3))
    if int(round((max_-min_)/min_, 2)*100) > int(threshold):
        print('Колебания цены за контрольный период БОЛЕЕ', threshold, "%  !!!")
        print('--------------------------------------------------')
    else:
        print('Колебания цены за контрольный период  НЕ БОЛЕЕ', threshold, "%  !!!")
