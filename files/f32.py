with open("Poem.txt", "r") as f1, open("CopiedPoem.txt", "w") as f2:
    for line in f1:
        f2.write(line)
