import os

folder_path = 'D:\\Python'

file_path = folder_path + '\\firsttextfile.txt'

try:
    os.remove(file_path)
    print('File removed successfully.')
except FileNotFoundError:
    print('The file does not exist')

try:
    os.remove(file_path)
except FileNotFoundError:
    print('The file does not exist (confirmed).')
