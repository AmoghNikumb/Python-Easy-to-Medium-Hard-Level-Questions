try:
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    assert b != 0, "Assertion Error: Cannot divide by zero."
    result = a / b
    print(result)
except (ValueError, AssertionError):
    print("Invalid integers")
