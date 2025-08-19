lucky = 10
chances = 3

for i in range(chances):
    num = int(input(f'Attempt {i+1}: Please enter your number: '))
    if num == lucky:
        print('You are lucky')
        break
    else:
        if i < chances - 1:
            choice = input('Do you want to try again? (Y/N): ')
            if choice.lower() == 'n':
                break
else:
    print('Out of chances!')

print('Have a nice day')
