import os

cwd = os.getcwd()
print("Current Working Directory:", cwd)

print("Current Working dir\n", os.listdir(cwd))

print(os.listdir("C:\\Users\\ADMIN\\OneDrive\\Desktop\\Website"))

os.chdir("C:\\Users\\ADMIN\\OneDrive\\Desktop\\Website")
print("Changed directory:", os.getcwd())
