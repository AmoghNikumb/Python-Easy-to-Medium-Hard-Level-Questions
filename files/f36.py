
with open("poem.txt", "r") as file:
    content = file.read()                   
words = content.split()
with open("words.txt", "w") as file:
    for word in words:
        file.write(word + "\n")
print("Words have been written to words.txt.")