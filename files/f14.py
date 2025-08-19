with open("LineFile.txt", "r") as file:
    line = file.readline()

reversed_line = line[::-1]

with open("LineFileNew.txt", "w") as new_file:
    new_file.writelines(reversed_line)

print("Lines have been reversed and saved to LineFileNew.txt")
