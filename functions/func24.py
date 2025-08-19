def Power(a, b=2):
    if b == 0:
        return 1
    return a * Power(a, b - 1)

print(Power(2))  
print(Power(5, 0)) 
