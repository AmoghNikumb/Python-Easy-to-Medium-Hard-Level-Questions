# This will open the file in read mode
# file pointer = open(<"File path">, mode ='r')
# D:\Python Evening Batch\File IO
f = open('First Text File.txt',\
         mode = 'r')

# It will read all the bytes of the file
x = f.read()
print("x = ", x)

y = f.read()
print('y', y)

f.seek(0)
y = f.read(10)
print('y', y)
