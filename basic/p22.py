CP=int(input("Enter the cost price:"))
SP=int(input("Enter the selling price:"))
if (SP>CP):
    print("Profit is",SP-CP)    
elif (SP<CP):
    print("Loss is",CP-SP)