def pass_gen ():
    import secrets
    import string
    
    print('Would you like to generate password automatically?\n\n')
    
    replies=['a','m']
    x = input('Press "a" for automatic generation\nPress "m" for manual generation\n')
    
    while x not in replies:
          x = input('Error, press "a" or "m": ')
    
    if x == 'a':
        while True:
            # Add here exception handling in case inputed length is not an integer number
            length = int(input('Choose length os password: '))
            if length > 4:
                break
            else:
                print("Password can't be less than 5 characters, try more.")
        
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(alphabet) for i in range(length))
    elif x == 'm':
        while True:
            # Add here exception handling in case inputed length is not an integer number
            length = int(input('Choose length os password: '))
            if length > 2:
                break
            else:
                print("Password can't be less than 3 characters, try more.")
        
        replies_2 = ['y','n']
        
        while True:
            letters = input('Letters in password? y/n: ')
            while letters not in replies_2:
                letters = input('Error, enter "y" or "n": ')
            
            digits = input('Digits in password? y/n: ')
            while digits not in replies_2:
                digits = input('Error, enter "y" or "n": ')
        
            spc_char = input('Special characters in password? y/n: ')
            while spc_char not in replies_2:
                spc_char = input('Error, enter "y" or "n": ')
            
            if 'y' in (letters,digits,spc_char):
                break
            else:
                print('At least one kind of symbols has to be present in password content\nTry again.\n')
            
        alphabet = ''
            
        if letters == 'y':
            alphabet += string.ascii_letters
        
        if digits == 'y':
            alphabet += string.digits
            
        if spc_char == 'y':
            alphabet += string.punctuation
        
        return ''.join(secrets.choice(alphabet) for i in range(length))