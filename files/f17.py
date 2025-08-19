
filename = "MyFirstFile.txt"  

try:
    with open(filename, "r") as file:
        content = file.read()
        space_count = content.count(" ")
        print(f"Number of spaces in '{filename}' is: {space_count}")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
