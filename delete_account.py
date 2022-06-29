def delete_account():
    import os
    
    list_of_accounts = os.listdir()
    
    for x in list_of_accounts:
        if '.txt' not in x:
            list_of_accounts.remove(x)
    if len(list_of_accounts) == 0:
        print('There are no accounts, please, create one!')
        return
    
    while True:
        acc = input('Please enter Login to delete your account: ')
        if acc + '.txt' in list_of_accounts:
            
            reply = ''
            replies = ['y','n']
            while reply not in replies:
                reply = input('Are you sure you want to delete (y/n): ')
                if reply not in replies:
                    print('Only "y" or "n" inputs are allowed!')
            if reply == 'y':
                os.remove(acc + '.txt')
                print('You have deleted ' + acc)
                return
            else:
                return
        else:
            print('Such an account isn\'t found!')