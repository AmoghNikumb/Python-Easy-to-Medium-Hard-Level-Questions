string = input("Enter a string to be reversed: ")
tempstr = string
print("Original String:", tempstr)
max_len = len(tempstr)
string = ''
for cnt in range(max_len - 1, -1, -1):
    string = string + tempstr[cnt]
print("Reversed String:", string)
