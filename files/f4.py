f = open('First Text File.txt',\
         mode = 'r')

# It will read all the bytes of the file
x = f.read()
print("x = ", x)

y = f.read()
print('y', y)

# f.seek(0)
# y = f.read(10)
