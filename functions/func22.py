def series_sum(n):
    total = 0
    for i in range(2, n + 1):
        total += 1 / i
    return total
print(series_sum(5))  
