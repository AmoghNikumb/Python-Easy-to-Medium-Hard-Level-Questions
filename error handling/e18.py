def indexException (obj1, n) :
    p = 0
    q = len(obj1) - 1
    #q = 3

    if (n >= p and n < q) :
        return (obj1[n])
    else :
        raise IndexError ("The index should be between " ,\
                          p , " and ", q)

##############################################

List1 = [1, 2, 3, 4, 5]
print (indexException (List1, 2))
indexException (List1, 5)

'''
x = 5
y =4
print (f"This is my format string {x} which is greater than {y}")
'''
