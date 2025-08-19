def Number():
    try:
        num = int(input("Enter a number: "))
        if (num >= 0):
            print("The number is:", num)
        else:
            raise ValueError("Number is less than 0")
    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)

Number()
