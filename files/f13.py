with open ('File2.txt','r') as File1:
    lines=File1.read()
    print(lines)
    words=lines.split()
    print(len(words))
