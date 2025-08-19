def indexException(obj1, n) :

    try :
        return (obj1[n])
    except IndexError :
        p = 0
        q = len(obj1) - 1
        return ("The index should be between ", \
                p , " and ", q)
    except TypeError :
        return ('The object is not an ordered collection of elements')
    except KeyError :
        return ('Key not found')

List1 = [1, 2, 3, 4, 5]
print (indexException (List1, 2))
print (indexException (List1, 5))

x = 5
print (indexException (x, 2))

Dict1 = {1 : 'abc', 2 : 'def', 3 : 'ghi'}
print (indexException (Dict1, 2))
print (indexException (Dict1, 4))
