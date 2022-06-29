def main():
    import os
    #from IPython.display import clear_output
    #import sys
    
    parent_dir = os.getcwd()
    
    #sys.path.insert(1, parent_dir)
    try:
        os.chdir('Accounts')
    except:
        os.mkdir('Accounts')
    
    actions = ['a','c','d','s','q']
    
    while True:
        print('Current directory is:\n' + os.getcwd()+'\n\n')
        action = input('Would you like to\n\n\
        Create account (c): \n\
        Access account (a): \n\
        Delete account (d): \n\
        Show list of accounts (s): \n\
        Quit (q): \n')
        
        
        if action == 's':
            from list_of_accounts import print_list_of_accounts
            print_list_of_accounts()
            input('Press enter to continue.')
            
        #clear_output(wait=True)
        os.system('cls' if os.name == 'nt' else 'clear')
        if action == 'c':
            
            from create_encrypted_account import create_account as CA
            CA()
            
        if action == 'd':
            from delete_account import delete_account
            delete_account()
        
        if action == 'a':
        
            from get_account import access
            account_name = access()
            
            if account_name is None:
                continue
            else:
                print('Account ' + account_name + ' found\n')
                from get_encrypted_data import get_data
                account_data = get_data(account_name)
                
                Data = account_data[0]
                Salt = account_data[1]
                Password = account_data[2]
               
                
                while True:
                    
                    ToDoList = ['f','c','a','d','l','s']
                    ToDo = ''
                    ToDo = input('This is account: ' + account_name +'\''
                                   '\nWhat would you like to do\n\n\
                                    Show all websites for which logins are stored: (s)\n\
                                    Find login data (f): \n\
                                    Change login data (c): \n\
                                    Add login data (a): \n\
                                    Delete login data (d): \n\
                                    Quit account (q); \n\
                                ')
                    #clear_output(wait=True)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if ToDo == 's':
                        set_of_websites = set()
                        for i in range(len(Data)):
                            set_of_websites.add(Data[i]['Website'])
                        print('List of websites: ')
                        print(set_of_websites)
                        
                    if ToDo == 'q':
                        break
                    
                    if ToDo == 'f':
                        from FindLogin import find_login_data
                        find_login_data(Data)
                        
                    if ToDo == 'a':
                        from add_data import add_login_data
                        add_login_data(Data)
                    
                    if ToDo == 'd':
                        from FindLogin import find_login_data
                        Data.pop(find_login_data(Data))
                    
                    if ToDo == 'c':
                        from FindLogin import find_login_data
                        position = find_login_data(Data)
                        
                        if position == -1:
                            print('Couldn\'t find')
                        else:
                            from Login_Password_Modify import change_login_data
                            change_login_data (position, Data)
                    
                    if ToDo not in ToDoList:
                        print('Type only "c", "a" or \"q\",\n\
                                    other inputs are not acceptable!')
                        #clear_output(wait=True)
                        os.system('cls' if os.name == 'nt' else 'clear')
                
            from decrypt_and_close_account import close_account
            close_account (account_name, Data, Salt, Password)
            
            #close_account(account_name, account_data)
                
            
        if action == 'q':            
            print('Good buy!')
            
            os.chdir(parent_dir)
            
            print('Current directory is:\n' + os.getcwd()+'\n')
            
            return
        
        if action not in actions:
            print('Type only "c", "a" or \"q\",\n\
                    other inputs are not acceptable!\
                    ')
        

        
    os.chdir(parent_dir)
    #clear_output()
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Current directory is:\n' + os.getcwd()+'\n')