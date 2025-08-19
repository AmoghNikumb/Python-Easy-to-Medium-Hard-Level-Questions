cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
assert selling_price > cost_price, "Assertion Error: Sale is not profitable."
print("Profit made on sale!")
