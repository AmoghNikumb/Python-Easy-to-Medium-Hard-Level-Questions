lucky = 10
while (1):
    num = int(input('Please enter your number : '))
    if (num == lucky):
        print('You are lucky')
        break
    choice = input('Do you want to continue : ')
    if ((choice == 'N') or (choice == 'n')):
        break

print('Have a nice day')
