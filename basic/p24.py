#Accept Marks in Maths, Science and English. Find the percentage and print
#whether 'First class' or not
m=int(input("Enter marks in Maths: "))
s=int(input("Enter marks in Science: "))
e=int(input("Enter marks in English: "))
total=m+s+e
per=total/3
print("Total marks are ",total)
print("Percentage is ",per)
if (per>=60):
    print("First class")
else:
    print("Not First class")
