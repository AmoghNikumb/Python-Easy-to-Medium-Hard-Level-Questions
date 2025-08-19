def HighSalesProducts(prod_dict):
    high_sales = {}
    total = 0
    for product, amount in prod_dict.items():
        total += amount
        if amount > 10000:
            high_sales[product] = amount

    average_sales = total / len(prod_dict)
    return high_sales, average_sales
Prod_sales = {
    'TV': 40000,
    'Pen drive': 2000,
    'Lap Top': 15000,
    'Mouse': 200,
    'DeskTop': 50000
}
result = HighSalesProducts(Prod_sales)
print("Products with sales > 10000:", result[0])
print("Average sales:", result[1])
