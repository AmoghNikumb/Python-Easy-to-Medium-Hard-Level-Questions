negative = 0
positive=0
zeros =0

for i in range(10):
    num = float(input("Enter number " + str(i + 1) + ": "))
    if num < 0:
        negative += 1
    if num >0:
        positive+=1
    if(num==0):
        zeros+=1        

print(f"Count of negative numbers: {negative}")
print(f"Count of positive numbers: {positive}")
print(f"Count of zeros: {zeros}")
