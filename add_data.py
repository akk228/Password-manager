def add_login_data (account_data):
    from unicity import is_unique
    success = False
    website = input('Enter the website: ')
    while not success:
        login = input('Enter the login: ')
        new_data = dict({'Website': website, 'Login': login, 'Password': ''})
        if is_unique(new_data, account_data) == True:
            reply = ''
            replies = ['y','n']
            
            while reply not in replies:
                reply = input('If you want to compose password yourself type y \nIf you want to use password generator type n \n\
                            ')
                if reply not in replies:
                    print('Only "y" or "n" inputs are allowed!')

            if reply == 'y':
                new_data['Password'] = input('New password is: ')

            if reply == 'n':
                from pass_gen import pass_gen
                new_data['Password'] = pass_gen()
                print('New password is: ' + new_data['Password'])
                
            print('New login data added!\n\n')
            
            account_data.append(new_data)
            
            success = True
        else:
            reply = ''
            replies = ['y','n']
            
            while reply not in replies:
                reply = input('Wanna try one more time?')
                if reply not in replies:
                    print('Only "y" or "n" inputs are allowed!')
            if reply == 'y':
                continue
            else:
                return        
