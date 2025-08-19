def GetValue(x, y, operator='+'):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y if y != 0 else "Division by zero error"
    else:
        return "Invalid operator"
print(GetValue(10, 5)) 
print(GetValue(10, 5, '*'))   
print(GetValue(10, 5, '-'))  
