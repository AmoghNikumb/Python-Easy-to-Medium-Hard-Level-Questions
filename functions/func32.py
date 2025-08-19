def ListToDict(lst):
    dict1 = {item: index for index, item in enumerate(lst)}
    return dict1
list1 = ['dahlia', 'jasmine', 'rose', 'lotus']
result = ListToDict(list1)
print("Dictionary:", result)
print("\nKeys and Values:")
for key, value in result.items():
    print("Key:", key, "| Value:", value)
