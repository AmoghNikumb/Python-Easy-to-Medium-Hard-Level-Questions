file = open('FirstTextFile.txt', 'r')

while True:
    chunk = file.read(5)
    print(chunk)
    if not chunk:
        break

file.close()
