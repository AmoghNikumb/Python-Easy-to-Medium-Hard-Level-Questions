import math

def SquareRoot(Num):
    try:
        if Num < 0:
            raise ValueError("Cannot compute square root of a negative number")
        return math.sqrt(Num)
    except ValueError as e:
        print("ValueError:", e)
        return None
print("Square root:", SquareRoot(25))
print("Square root:", SquareRoot(-9))
