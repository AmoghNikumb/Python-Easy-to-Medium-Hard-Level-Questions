States = ['Maharastra', 'Goa', 'Punjab', 'Haryana', 'Rajasthan']
Capitals = ['Mumbai', 'Panaji', 'Chandigard', 'Chandigard', 'Jaipur']

Dict1 = {States[cnt]: Capitals[cnt] for cnt in range(len(States))}
print(Dict1)