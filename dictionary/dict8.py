List1 = [1, 4, 9, 16, 25]
Dict1 = {i ** 0.5 : i for i in List1}

print(Dict1)             
print(Dict1.keys()) 

if (3 in Dict1):
    print(Dict1[3])
else:
    print('Not found')
