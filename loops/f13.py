string = input("Enter a string to reverse it")
print(len(string))
x=len(string)
for char in range(x-1,-1,-1):
    print(string[char],end='\t')