
# ============  Вариант 1  ==============
# def calculate_and_display_average_price(data):
#     x = 0
#     i = 0
#     for s in data["Close"].values:
#         i += 1
#         x += s
#     print('--------------------------------------------------')
#     print('Average closed price for period  is:', round(x/i,3))
#     print('--------------------------------------------------')

# ============  Вариант 2  ==============
def calculate_and_display_average_price(data):
    x = data['Close'].mean()

    print('--------------------------------------------------')
    print('Average closed price for period  is:', round(x, 3))
    print('--------------------------------------------------')

