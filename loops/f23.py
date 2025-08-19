numbers = []

for i in range(5):
    num = int(input("Enter numbers1 : "))
    numbers.append(num)

minimum = numbers[0]

for i in range(1, 5):
    if numbers[i] < minimum:
        minimum = numbers[i]

print("The minimum number is:", minimum)
