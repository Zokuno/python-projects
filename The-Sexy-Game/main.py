def the_game():
    print('Welcome to the sexy guessing game! To win, simply answer who the sexiest person is!')
    print('')
    print('So, who is the sexiest?')
    while input() != 'Shellby':
        print('Wrong! Try again!')
        continue
    else:
        print('Well done! You are correct! Play again?')
    if input() == 'Yes':
        the_game()
    elif input() == 'No':
        print('Thanks for playing!')
        sys.exit
    else:
        print('Please enter \'Yes\' or \'No\'')
        
def repeat():
    if input() == 'Yes':
        print(intro)
        the_game()
    elif input() == 'No':
        print('Goodbye')
        sys.exit()
    else:
        print('Please type yes or no')

the_game()