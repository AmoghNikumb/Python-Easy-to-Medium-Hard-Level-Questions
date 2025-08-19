str1 = input("Enter elements of list seperated by , :")
print(str1)
print(str1.split(', '))
list1=[]
for cnt in str1.split(', '):
    list1.append(int(cnt))
print("list is now: ",list1)    
