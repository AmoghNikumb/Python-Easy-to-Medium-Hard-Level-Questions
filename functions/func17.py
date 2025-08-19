def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
hcf = find_hcf(30,40)
print("HCF:", hcf)
