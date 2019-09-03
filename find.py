from forex_python.converter import CurrencyRates

c = CurrencyRates()
price = input("Enter amount ($): ")

coins = c.get_rates('USD') 
for key, value in coins.items():
    v = lambda x : round(float(x)*value,2)
    y = v(price)

    if y > 1000000:
        print(str(key) + " " + str(y))

