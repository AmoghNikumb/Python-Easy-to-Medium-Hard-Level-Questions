def addTen():
    try:
        value = input("Enter a number: ")
        number = float(value)
        return number + 10
    except ValueError:
        print("ValueError: Input is not a valid number.")
        return None
result = addTen()
print("Result:", result)
