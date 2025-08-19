students=[
    ('Vikas',90),
    ('Shardul',89),
    ('Amogh',95),
]
with open("studeny_manual.dat","wb") as f:
    for name,marks in students:
        line=f"{name}|{marks}\n"
        f.write(line.encode('utf-8'))
print("Data Written in Binary form")        