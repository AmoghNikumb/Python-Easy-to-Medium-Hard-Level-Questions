English = int(input("Enter marks of English"))
Maths = int(input("Enter marks of Maths"))
Science = int(input("Enter marks of Science"))
sum = English+Maths+Science
percentage = (sum)/300*100
print("Total Marks Secured: ",sum)
print("Percentage Secured: %",percentage)
if(percentage > 90):
    print("A+")
elif(percentage >80):
    print("A")
elif(percentage>70):
    print("B+") 
elif(percentage>60):
    print("B")
else:
    print("Fail")               