def remove_duplicates(list1): #
    return list(dict.fromkeys(list1))

List1 = [5, 23, 1, -90, -90, 3, 5, 5, 23, 78]
print(remove_duplicates(List1))
