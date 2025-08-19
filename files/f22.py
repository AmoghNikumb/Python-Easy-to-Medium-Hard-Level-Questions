with open('studeny_manual.dat') as f:
    content = f.read()

lines = content.strip().split('\n')
for line in lines:
    name, marks = line.split('|')
    print(name, marks)
