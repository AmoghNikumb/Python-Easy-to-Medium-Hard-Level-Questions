print("Table of 2:")
for i in range(1, 11):
    print("2 x " + str(i) + " = " + str(2 * i))
print() 
n = int(input("Enter a number to print its multiplication table: "))
print("Table of " + str(n) + ":")
for i in range(1, 11):
    print(str(n) + " x " + str(i) + " = " + str(n * i))
