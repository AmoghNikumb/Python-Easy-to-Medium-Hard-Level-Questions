import os
import datetime as dt

path = 'D:\Python\firsttextfile.txt'
RemoveFile = path + '\\assignmentsCurrentDate.txt'

try:
    os.remove(RemoveFile)
    print('After remove')
    print(os.listdir(path))
except FileNotFoundError:
    print('The file does not exist')
