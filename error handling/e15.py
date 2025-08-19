def Divide(a, b):
    try:
        num = a / b
        print("Result:", num)
    except ZeroDivisionError:
        print("Number is divided by zero... division not possible.")
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    Divide(x, y)
except ValueError:
    print("Invalid input! Please enter integers only.")
           
