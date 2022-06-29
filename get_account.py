def access():
    import os
    #from IPython.display import clear_output
    list_of_accounts = os.listdir()
    
    for x in list_of_accounts:
        if '.txt' not in x:
            list_of_accounts.remove(x)
    if len(list_of_accounts) == 0:
        print('There are no accounts, please, create one!')
        #clear_output(wait=True)
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    
    while True:
        acc = input('Please enter Login to access your account: ')
        if acc + '.txt' in list_of_accounts:
            print('You have accessed ' + acc)
            return acc
        else:
            reply = ''
            replies = ['y','n']
            while reply not in replies:
                reply = input('There is no such account!\nWould you like to continue? (y/n): ')
                #clear_output(wait=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                if reply not in replies:
                    print('Only "y" or "n" inputs are allowed!')
                    #clear_output(wait=True)
                    os.system('cls' if os.name == 'nt' else 'clear')
            if reply == 'y':
                pass
            else:
                return