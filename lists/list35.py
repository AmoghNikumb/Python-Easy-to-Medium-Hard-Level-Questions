n = int(input("Enter how many multiples of 10 you want: "))
multiples_of_10 = []
for i in range(1, n + 1):
    multiples_of_10.append(i * 10)
print("First", n, "multiples of 10:", multiples_of_10)
