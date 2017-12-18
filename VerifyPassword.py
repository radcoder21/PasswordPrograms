def numberCheck(character):
    try:
        if int(character) == eval(character):
            return True
    except:
        return False

def letterCheck(character):
    try:
        if character == character.lower():
            return True
    except:
        return False

def capitalCheck(character):
    if character == character.upper():
        return True
    else:
        return False

def Length(password):
    if len(password) >= 8 and len(password)<=16:
        return True
    else:
        return False

def Main():
    print('This program will create a password.\n')
    print('Please enter a password that is 8-16 characters long with atleast\none number and atleast one capital letter.\n')
    letters = 0
    capital = 0
    number = 0
    password = ''
    while password == '':
        password = input('Input your password: ')
        if Length(password):
            for character in password:
                if numberCheck(character) and number == 0:
                    number += 1
                elif capitalCheck(character) and capital == 0:
                    capital += 1 
                elif letterCheck(character) and letters == 0:
                    letters += 1
                    if letters > 0 and capital > 0 and number > 0:
                        print('\nYou succesfully created your password!\n')
                        print('Your password is: ', password)
                    else:
                        print('\nYour password did not follow the specifications.\n')
                        print('Please Try Again\n')
                        password = ''
        else:
            print('\nYour password is not 8-16 characters long.\n')
            print('Please Try Again\n')
            password = ''

Main()

            
        
        
