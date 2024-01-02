import currency_converter as currency_converter
#pip install CurrencyConverter
c = currency_converter.CurrencyConverter()
#convert USD to EUR
print(c.convert(1, 'EUR', 'USD'))