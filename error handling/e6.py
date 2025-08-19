try:
    num = float(input("Enter a number: "))
    if num < 0:
        raise ValueError("Number is negative")
    else:
        print("You entered:", num)
except ValueError as ve:
    print("ValueError:", ve)
