ResultList=[]
try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    sum=a+b
except ValueError:
    sum='Not an Integer'
except:
    print("Error has occured!")    
finally:
    ResultList.append(sum)
print("Result: ",ResultList)    

