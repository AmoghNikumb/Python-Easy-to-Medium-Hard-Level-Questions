def GetElement(Obj1, index):
    if (type(Obj1) == list or type(Obj1) == tuple):
        if (index >= 0 and index < len(Obj1)):
            x = Obj1[index]
        else:
            x = ""
    elif (type(Obj1) == dict):
        x = Obj1.get(index, "")
    else:
        x = ""
    return x
List1 = [10, 20, 30, 40, 50]
print('4th element of List1 :', GetElement(List1, 4))      
print('10th element of List1 :', GetElement(List1, 10))    
Dict1 = {10: 'ABC', 20: 'DEF'}
print('Value for 10 :', GetElement(Dict1, 10))             