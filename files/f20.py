with open("studeny_manual.dat","rb") as f:
    content=f.read()
    decoded_content=content.decode('utf-8')
lines=decoded_content.strip().split('\n')
for lines in lines:
    name,marks=lines.split('|')
    print(f'Names: {name}|Marks: {marks}')     