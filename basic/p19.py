# Accept 2 nos from the user and print their average if their sum is > 100
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if (a+b>100):
    print("Average of a and b is ",(a+b)/2)
else:
    print("Sum of a and b is ",a+b)
