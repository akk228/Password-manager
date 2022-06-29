def print_list_of_accounts():
    import os
    
    list_of_accounts = os.listdir()
    
    for x in list_of_accounts:
        if '.txt' not in x:
            list_of_accounts.remove(x)
    if len(list_of_accounts) == 0:
        print('There are no accounts, please, create one!')
        return
    
    print(list_of_accounts)