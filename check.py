from nsetools import Nse
nse = Nse()
all_stock_codes = nse.get_stock_codes()
for i in all_stock_codes :
    print(i)
