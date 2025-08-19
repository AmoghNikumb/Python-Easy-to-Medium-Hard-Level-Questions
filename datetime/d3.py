from datetime import date

current_date1 = date.today()
print('Today is ', current_date1)
print(type(current_date1))

current_date1 = date.today().strftime('%d-%m-%Y')
print('Today is ', current_date1)
print(type(current_date1))

current_date1 = date.today().strftime('%d/%m/%Y')
print('Today is ', current_date1)
print(type(current_date1))
