States = ['Maharastra', 'Goa', 'Punjab', 'Haryana', 'Rajasthan']
Capitals = ['Mumbai', 'Panaji', 'Chandigard', 'Chandigard', 'Jaipur']

Dict1 = {}
for cnt in range(0, len(States)):
    Dict1.update({States[cnt]: Capitals[cnt]})

print(Dict1)
