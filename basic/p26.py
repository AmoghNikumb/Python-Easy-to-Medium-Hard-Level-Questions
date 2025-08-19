a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=int(input("Enter value of c"))
D = (b*b - 4*a*c)
print(D)
denominator = (2*a)**0.5
if(D>0):
    print("Roots are real: ")
    print((-b+D**0.5)/denominator)
    print((-b-D**0.5/denominator))