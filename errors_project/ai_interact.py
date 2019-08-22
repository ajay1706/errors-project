def interact():
    while True:
        user_input = int(input("enter a value: "))
        isEven = user_input %2 == 0
        print('{} is {}'.format(user_input, 'even' if isEven else 'odd'))

        user_input = input('Do you want to play again (Y/N)? ')

        if user_input!= 'y':
            print('Good bye')
            break
print(interact())