def MinMax():
    for i in range(5):
        num = int(input("Enter number " + str(i + 1) + ": "))
        if i == 0:
            minimum = maximum = num
        else:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num

    print("Minimum number is:", minimum)
    print("Maximum number is:", maximum)

MinMax()

