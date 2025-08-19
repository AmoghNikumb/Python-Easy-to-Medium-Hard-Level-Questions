a=int(input("Enter a number to print its power"))
b=int(input("Enter its power"))
result=1
cnt=0
while(cnt<b):
    result*=a
    cnt +=1
print(f"{a} to the power {b} is:{result}")    