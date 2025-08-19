while True:
    num = int(input("Enter a number to find its factorial: "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "is", fact)
    
    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        print("Exiting program.")
        break
