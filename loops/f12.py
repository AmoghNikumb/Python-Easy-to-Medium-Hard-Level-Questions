user_input = input("Enter a string: ")
alternate_chars = ""
for i in range(0, len(user_input), 2): 
    alternate_chars += user_input[i]
print("Alternate characters:", alternate_chars)
