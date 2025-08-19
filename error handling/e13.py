import random
try:
    num = random.random()  
    if (num < 0.1):
        raise ValueError("Generated number is too small: " + str(num))
    print("Generated number:", num)
except ValueError as e:
    print("Exception:", e)
