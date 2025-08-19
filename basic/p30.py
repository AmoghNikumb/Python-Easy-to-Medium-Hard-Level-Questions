s1=int(input("Enter side of triangle"))
s2=int(input("Enter side2 of triangle"))
s3=int(input("Enter side3 of triangle"))
if(s1==s2 and s2==s3 and s1==s3):
    print("Equilateral Triangle")
elif(s1!=s2 and s2!=s3 and s1!=s3):
    print("Scalene Triangle")
else:
    print("Isosceles Triangle")        