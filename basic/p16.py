#Accept cordinates of 2 points and print the distance between the two points
x1=int(input("Enter x1 coordinate: "))
y1=int(input("Enter y1 coordinate: "))
x2=int(input("Enter x2 coordinate: "))
y2=int(input("Enter y2 coordinate: "))
distance=((x2-x1)**2+(y2-y1)**2)**0.5
print("Distance between the two points is ",distance)