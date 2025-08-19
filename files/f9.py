file = open('FirstTextFile.txt', 'r')
content = file.read()
words = content.split()
for word in words:
    print(word)

file.close()
