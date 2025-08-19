list = []
for i in range(1,11):
    print(i)
    list.append(i)
print(list)
for i in list:
    if(i%2==0):
        list.remove(i)
print("New list is :",list)            