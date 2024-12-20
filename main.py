import data_download as dd
import data_plotting as dplt
import matplotlib.pyplot as plt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: "
          "AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), "
          "AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, "
          "2г, 5г, 10л, " "с начала года, макс.")
    print()
    print(' ============= Ввод  исходных  данных ==================')
    print()
    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    x = input("Выберите диапазон дат анализа  данных - период ('P')  либо даты начала и конца ('D) ")
    print(x)
    if x.lower() == 'p':
        period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    else:
        start = input("Введите дату начала анализа в формате Y-M-D): ")
        end = input("Введите дату конца анализа в формате Y-M-D): ")
        period = start + '_' + end

    threshold = input("Введите порог оценки колебаний цены в %:")

    print("Возможные стили графиков:  ")
    # i = 0
    # for s in plt.style.available:
    #     print(i, s)
    #     i += 1

    i = int(input("Введите номер желательного стиля графика 'style' из  приведенного списка(0,4,5,8,9,11,16,26):"))
    style = plt.style.available[i]
    print('style =', style)
    print()
    print("******************** POGRAMM  START *****************************")
    print()

    # Fetch stock data
    if x.lower() == 'p':
        stock_data = dd.fetch_stock_data('Googl', period='1mo')
    else:
        stock_data = dd.fetch_stock_data_1(ticker, start, end)

    # Generate filename and save DataFrame in .csv format
    filename = f"{ticker}_{period}_DataFrame.csv"
    dd.export_data_to_csv(stock_data, filename)

    # Add moving average column to the data frame
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data and save in .png file
    dplt.create_and_save_plot(stock_data, ticker, period, style)

    # Average Closed data calculation
    dd.calculate_and_display_average_price(stock_data)

    # Price fluctuation  analysis
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Standard_deviation of Closed price calculation
    st_dev = dd.calculate_and_display_standard_deviation(stock_data)

    # RSI  calculftion
    rsi = dd.rsi_calculation(stock_data)
#    print(rsi)

    # Plot "Close"  and "RSI" data and save in .png file
#    filename_ = f"{ticker}_{period}_RSI_chart.png"
    dplt.create_and_save_rsi_plot(stock_data, ticker, period, rsi, style)


if __name__ == "__main__":
    main()
