import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: "
          "AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), "
          "AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, "
          "2г, 5г, 10л, " "с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = input("Введите порог оценки колебаний цены в %:")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)
#    print(stock_data)

    # Generate filename and save DataFrame in .csv format
    filename = f"{ticker}_{period}_DataFrame.csv"
    dd.export_data_to_csv(stock_data, filename)

    # Add moving average column to the data frame
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data and save in .png file
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Average Closed data calculation
    dd.calculate_and_display_average_price(stock_data)

    # Price fluctuation  analysis
    dd.notify_if_strong_fluctuations(stock_data, threshold)


if __name__ == "__main__":
    main()
