def SumDiffProd(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    return sum_result, diff_result, prod_result

# Example usage:
s, d, p = SumDiffProd(10, 5)
print("Sum:", s)
print("Difference:", d)
print("Product:", p)
