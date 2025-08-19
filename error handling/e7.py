try:
    num=10
    print(num)
    raise(ValueError)
except:
    print("Re-raising exception ")
    raise
else:
    print("Have a good day!")