def create_account():
    from getpass import getpass
    #from IPython.display import clear_output
    import json
    import base64
    import os
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    
    unique = False
    
    #Get the list of already exisiting accounts
    
    list_of_accounts = os.listdir()
    
    #Check if the new account name is unique
    
    while not unique:
        login = input('Please enter login: ')
        if login + '.txt' in list_of_accounts:
            reply = ''
            replies = ['y','n']
            while reply not in replies:
                reply = input('Login exists!\nWould you like to continue? (y/n): ')
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
        else:
            unique = True
    
    # If we haven't given up trying to create account,
    # Here it is getting created!
    
    # First we compose password for the account
    
    passwords_are_same = False
    
    while not passwords_are_same:
        password1 = getpass('Enter password: ')
        password2 = getpass('Repeat password: ')
        if password1 == password2:
            passwords_are_same = True
        else:
            print('Passwords do not match, try again!')
            #clear_output(wait=True)
            os.system('cls' if os.name == 'nt' else 'clear')
    print('Passwords matched, succesful!')
    #clear_output(wait=True)
    os.system('cls' if os.name == 'nt' else 'clear')
    # That is salt for future key generation
    # Here we put an encrypted empty list to initialize ecncrypted account with the password
    
    Salt = os.urandom(16).hex()
    
    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=Salt.encode(),
                        iterations=10000,
                    )
    
    key = base64.urlsafe_b64encode(kdf.derive(password1.encode()))
    
    fer = Fernet(key)
    token = fer.encrypt(b"[]")
    
    with open(login + '.txt','w') as file:
        file.write(Salt + '\n')
        file.write(token.decode())