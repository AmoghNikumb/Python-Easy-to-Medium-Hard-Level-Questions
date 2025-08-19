
num = int(input("Enter a number: "))

factors = {i for i in range(1, num + 1) if num % i == 0}

if factors == {1, num}:
    print(str(num) + " is a prime number.")
else:
    print(str(num) + " is not a prime number.")
