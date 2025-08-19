def MinMaxAvg(sales):
    minimum = min(sales)
    maximum = max(sales)
    average = sum(sales) / len(sales)
    return minimum, maximum, average

Sales = [23, 45, 10, 12, -65, 2]
result = MinMaxAvg(Sales)
print(result) 

