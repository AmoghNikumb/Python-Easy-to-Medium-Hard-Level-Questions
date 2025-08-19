File1=open('File2.txt','r')
for line in File1:
    print(line)
File1.close()
status=File1.close()
print("File one has been closed!",status)