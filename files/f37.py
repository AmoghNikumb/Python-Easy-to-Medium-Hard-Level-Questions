#16. Write a Python program to assess if a file is closed or not using try and except without using function
try:
    file = open('poem.txt', 'r')
    print("File is open.")
except Exception as e:
    print("File is closed.")
    print(e)
    print("File is closed.")
finally:
    file.close()
    print("File has been closed.")