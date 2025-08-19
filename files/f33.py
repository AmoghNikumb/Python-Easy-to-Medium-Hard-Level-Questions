with open("poem.txt", "r") as file:
    content = file.read()

words = content.split()

longest_word = max(words, key=len)

print("The longest word is:", longest_word)
