while(1):
    a=input("Enter an interger.")
    b=0
    try:
        b=int(a)
    except:
        print("Type Error")
        continue
    else:
        break 
print(b)    
       