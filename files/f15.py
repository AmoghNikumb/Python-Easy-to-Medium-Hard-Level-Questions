lines=['Hello World','Welcome to Python','We are doing File Handling','Lets Create a File']
File1=open('File2.txt','w')
File1.writelines(lines)
File1.close()
print("End")
