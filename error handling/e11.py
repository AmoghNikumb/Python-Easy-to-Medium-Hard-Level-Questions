def GetElement(list, index):
    try:
        return list[index]
    except IndexError as e:
        return e  
    
#########################################################################
def GetList () :
    List1 = []
    str1 = input ("Please enter comma sepereated elements")
    List1 = str1.split (", ")
    return (List1)
################################################################

list1 = GetList()
print(GetElement(list1, 2)) 
print(GetElement(list1, 10))  
