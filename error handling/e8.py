try:
    raise Exception('Hello','World')
except Exception as ErrObj:
    print(ErrObj)
    print(type(ErrObj))
    arg1,arg2=ErrObj.args
    print("First Arguement ",arg1)
    print("Second Arguement ",arg2)