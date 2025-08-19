list =[]
print(list)
for i in range(1,21):
    if(i%2!=0):
        print(i)
        list.append(i)
print(list)        

list = [i for i in range(1, 21) if i % 2 != 0]
print(list)
