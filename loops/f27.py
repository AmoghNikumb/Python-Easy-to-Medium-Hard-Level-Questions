for i in range(1, 4):
    ch = 'A'
    for j in range(i):
        print(ch, end=' ')
        ch = chr(ord(ch) + 1)
    print()
