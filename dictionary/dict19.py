Prod_dict = {'Lap top': 50000, 'Mouse': 200, 'Pen drive': 300, 'Printer': 10000, 'Mobile': 15000}
prod_dict_5000 = {product : price for product, price in Prod_dict.items()
                  if price> 5000}
print(prod_dict_5000)