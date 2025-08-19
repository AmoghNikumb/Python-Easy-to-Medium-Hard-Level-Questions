def GetNegPos(numbers):
    pos_count = 0
    neg_count = 0
    for num in numbers:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_count += 1
    return pos_count, neg_count

# Example usage:
lst = [4, -1, 0, -7, 8, 5, -3]
pos, neg = GetNegPos(lst)
print("Positive numbers:", pos)
print("Negative numbers:", neg)
