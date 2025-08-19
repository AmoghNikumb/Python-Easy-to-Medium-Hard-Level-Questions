import os
cwd = os.getcwd()
print("Current Working Directory:", cwd)
print("Current Working dir\n", os.listdir(cwd))
print(os.listdir("C:/Users/ADMIN/OneDrive/Desktop/Website"))

'''
# You can uncomment this if you want to change directory
# os.chdir("C:/Users/ADMIN/OneDrive/Desktop/Website/Errors")
# print("Changed directory:", os.getcwd())
'''

os.chdir(cwd)
print("Changed back to directory:", os.getcwd())

# Remove a directory (make sure it exists and is empty)
# os.rmdir("TmpNew")  # Uncomment if directory exists and is empty
