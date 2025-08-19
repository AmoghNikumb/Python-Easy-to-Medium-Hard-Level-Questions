import datetime

filename = "ThirdLineFile.txt"
creator_name = "Amogh Nikumb"  

current_date = datetime.date.today().strftime("%d-%m-%Y")

file = open(filename, 'w')
file.write("1. File Name: " + filename + "\n")
file.write("2. Created By: " + creator_name + "\n")
file.write("3. Date Created: " + current_date + "\n")
file.close()
