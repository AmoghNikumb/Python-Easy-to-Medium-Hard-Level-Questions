import random
original_list = [random.randint(1, 100) for i in range(10)]
OddList = [num for num in original_list if num % 2 != 0]
EvenList = [num for num in original_list if num % 2 == 0]
print("Original List:", original_list)
print("Odd Numbers List:", OddList)
print("Even Numbers List:", EvenList)
