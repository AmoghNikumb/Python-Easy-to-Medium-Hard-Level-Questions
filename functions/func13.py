def HighSalesProducts(sales_dict):
    print("Products with sales more than 10000:")
    for product, amount in sales_dict.items():
        if amount > 10000:
            print(product)

if __name__ == "__main__":
    Prod_sales = {
        'TV': 40000,
        'Pen drive': 2000,
        'Lap Top': 15000,
        'Mouse': 200,
        'DeskTop': 50000
    }

    HighSalesProducts(Prod_sales)
