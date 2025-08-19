def TriangleType(a, b, c):
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return "Not a triangle"
    if (a == b == c):
        return "Equilateral"
    if (a == b) or (b == c) or (a == c):
        return "Isosceles"
    return "Scalene"
print(TriangleType(3, 3, 3)) 
print(TriangleType(3, 3, 2))  
print(TriangleType(3, 4, 5))  
