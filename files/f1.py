file1=open('firsttextfile.txt', mode='a')
str1 = 'This is mt text file. I have written in the textfile.This is my next fi;e'
file1.write(str1)
file1.close()
print("Success")