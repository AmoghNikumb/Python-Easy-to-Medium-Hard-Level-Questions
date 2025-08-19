def Divide(num,deno):
    try:
        quo=num/deno
        print("Quotient is ",quo)
    except(ZeroDivisionError):
        print("Raising exception...Program is terminating in the divide function..")
Divide(10,0)
print("Have a nice day!")
Divide(10,2)
print("End of Programme")            