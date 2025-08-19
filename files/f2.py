import datetime as dt

Date1 = dt.date.today()
Date1 = str(Date1)

Str1 = '\nI have modified it on ' + Date1

File1 = open('firsttextfile.txt', mode='a')
File1.write(Str1)
File1.close()
