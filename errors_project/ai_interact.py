def interact():
    while True:
        try:
            user_input = int(input("enter a value: "))
        except ValueError:
            print('PLease type integer only')
        else:
            print('{} is {}'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))
        finally:
            user_input = input('Do you want to play again? (Y/N): ')

        if user_input != 'y':
            print('Good bye')
            break


print(interact())