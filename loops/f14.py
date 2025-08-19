max1= -1
min1= 10000
num= 10000

for cnt in range(0,5):
    num=int(input("Enter 5 numbers"))
    if(num>max1):
        max1=num
    if(num<min1):
        min1=num
print("Maximum Number: ",max1,"Minimmum Number: ",min1)
print(max1-min1)        

'''
    cnt     num     max1    min1
            10000     -1    10000
      0      10        10   10
      1     5         10    5
      2     7       10      5

'''