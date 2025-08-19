def add_ten_if_number(value):
    try:
        number = float(value)
        return number + 10
    except ValueError:
        print("Error: Input is not a valid number.")
        return None

print(add_ten_if_number(5))      
print(add_ten_if_number("20"))  
print(add_ten_if_number("abc"))   
