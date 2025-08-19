list1 = [1, 2, 6, 0, 24, 8, 9, 10, -2, 100]
list2 = []

for element in list1:
    if element > 5:
        list2.append(element)

print("Elements greater than 5:", list2)
