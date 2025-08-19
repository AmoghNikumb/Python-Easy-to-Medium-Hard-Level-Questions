def FindPairWithSum(lst, n):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == n:
                return (lst[i], lst[j])
    return "No pair found"

print(FindPairWithSum([10, 20, 30, 40], 50))  
print(FindPairWithSum([1, 2, 3], 10))       
