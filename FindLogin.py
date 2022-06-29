def find_login_data(acc_data):
    Accounts_at_single_WS = []
    reply = ''
    replies = ['y','n']
    while True:
        website = input('Enter the web address: ')
        
        for i in range(len(acc_data)):
            if website in acc_data[i]['Website']:
                Accounts_at_single_WS.append(acc_data[i])
                
        if len(Accounts_at_single_WS) == 0:
            reply = ''
            while reply not in replies:
                reply = input('WebSite is not found!\n\
                                would you like to continue? (y/n): ')
                if reply not in replies:
                    print('Only "y" or "n" inputs are allowed!')
            if reply == 'y':
                pass
            else:
                return -1
        else:
            break
    
    
    while True:
        
        reply = ''
        while reply not in replies:
            reply = input('Want me to show all logins? (y/n): ')
            if reply not in replies:
                print('Only "y" or "n" inputs are allowed!')
        if reply == 'y':
            print('\nAll logins: \n')
            for log in Accounts_at_single_WS:
                print(log['Login'])
            print('\n')
        
        LoginList = []
        
        login = input('Enter the Login: ')
        for i in range(len(Accounts_at_single_WS)):
            if login in Accounts_at_single_WS[i]['Login']:
                LoginList.append(Accounts_at_single_WS[i]) 
                
        
        if len(LoginList) == 0 or login == '':
            reply = ''
            while reply not in replies:
                reply = input('Login is not found!\n\
                                would you like to continue? (y/n): ')
                if reply not in replies:
                    print('Only "y" or "n" inputs are allowed!')
            if reply == 'y':
                continue
            else:
                return -1
            
        
        if len(LoginList) > 1:
            print('Several logins are found!\n')
            reply = ''
            while reply not in replies:
                reply = input('Show all of them?\n')
                if reply not in replies:
                    print('Only "y" or "n" inputs are allowed!')
            if reply == 'y':
                print('List of logins for ' + LoginList[0]['Website'] + ': \n')
                for i in range(len(LoginList)):
                    print(LoginList[0]['Login'])
            print('To choose one of them, type the full login: ')
        
        if len(LoginList) == 1:
            reply = ''
            while reply not in replies:
                reply = input('Show password? (y/n): ')
                if reply not in replies:
                    print('Only "y" or "n" inputs are allowed!')
            if reply == 'y':
                print('\n\nAccount data:')
                print(LoginList[0])
                    
            return acc_data.index(LoginList[0])  