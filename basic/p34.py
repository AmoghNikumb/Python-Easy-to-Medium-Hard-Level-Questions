def Sum (*args) :
    '''
    Add the elements of a list or tuple or individual numbers
    '''

    total = 0

    if (type(args[0]) == list or type(args[0]) == tuple) :
        for cnt in args :
            total = 0
            for listCnt in cnt :
                try :
                    x = int (listCnt)

                except :
                    total = 'Wrong data type'
                    break
                else :
                    total += x
            return (total)

    elif (type (args[0]) == int) :
        for cnt in args :
            try :
                x = int (cnt)

            except :
                total = 'Wrong data type'
                break
            else :
                total += x
        return (total)