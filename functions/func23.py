def factorial_series_sum(n):
    def factorial(x):
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
    total = 0
    for i in range(2, n + 1):
        total += 1 / factorial(i)
    return total

print(factorial_series_sum(5))

