List1 = [1, 2, 3, 1, 1, 4, 5, 2, 4, 5, 3, 3, 3]
print("Count of 1 in list: ",List1.count(1))
print("Count of 3 in list: ",List1.count(3))
print("Count of 4 in list: ",List1.count(4))
if (1 in List1):
    print("Found")
else:
    print("Not found")
if ('abc' not in List1):
    print("Not Found")
else:
    print("Found")