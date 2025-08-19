n = 3 

with open("Poem.txt", "r") as file:
    lines = file.readlines()
    last_lines = lines[-n:] 

print("Stored lines:")
print(last_lines) 
