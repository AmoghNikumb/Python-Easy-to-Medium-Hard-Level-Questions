try:
    user_input = input("Enter a number: ")
    number = float(user_input) 
    print("Result:", number + 10)
except ValueError:
    print("ValueError: Input is not a valid number.")
