List1 = [10, 5, 8, 7, 5, 50, 4, 1, 2, 20]
List2 = [x + 6 if x % 2 == 0 else x + 4 for x in List1]
print(List2)
