number = int(input("Enter a number: "))
if(number%2==0):
    number = number-1
for num in range(number, 0, -1):
    if num % 2 != 0:
        print(num)
