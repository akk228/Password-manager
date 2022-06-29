def change_login_data (pos, account_data): 
    Data = dict(account_data[pos]) 
    while True: 
        actions = ['w','l','p'] 
        action = input('What would you like to change?\n\
                        Login?(l): \n\
                        Passowrd? (p): \n\
                        Nothing, I wanna quit (q): \n\
                        ') 
        if action == 'q': 
            return

        if action == 'p':
            reply = ''
            replies = ['y','n']
            while reply not in replies:
                reply = input('If you want to compose password yourself type y \n\
                            If you want to use password generator type n \n\
                            ')
                if reply not in replies:
                    print('Only "y" or "n" inputs are allowed!')

            if reply == 'y':
                Data['Password'] = input('New password is: ')

            if reply == 'n':
                from pass_gen import pass_gen
                Data['Password'] = pass_gen()
                print('New password is: ' + Data['Password'])

        if action == 'l':

            Data['Login'] = input('Enter new Login: ')

            from unicity import is_unique

            if is_unique(Data, account_data) == True:
                account_data[pos] = dict(Data)
                print("Login data is succesfully  changed!\n")
            else:
                print('There already exists account with similar login at this website!\n')

        if action not in actions:
            print('\nOnly q, l and p inputs are allowed!\n')
            
    account_data[pos] = dict(Data)