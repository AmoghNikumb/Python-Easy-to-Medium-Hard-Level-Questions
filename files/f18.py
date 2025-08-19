
source = input("Enter Python file name: ")
destination = "NoComments_" + source

with open(source, "r") as src, open(destination, "w") as dest:
    for line in src:
        if not line.lstrip().startswith("#"):
            dest.write(line)

print("New file created without comments.")
