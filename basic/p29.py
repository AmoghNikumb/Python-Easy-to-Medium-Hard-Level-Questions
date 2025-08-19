a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print(a, "is largest")
    else:
        print(c, "is largest")
else:
    if b > c:
        print(b, "is largest")
    else:
        print(c, "is largest")
