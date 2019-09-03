from forex_python.converter import CurrencyRates

c = CurrencyRates()
rate = c.get_rate('USD', 'EUR') 
print(rate)

price = input("Enter amount ($): ")

v = lambda x : round(float(x)*rate,2)
y = v(price)
print("\u20ac " + str(y))

