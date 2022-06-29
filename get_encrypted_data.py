def get_data (login):
    from getpass import getpass
    #from IPython.display import clear_output
    import json
    import base64
    import os
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    
    
    with open(login + '.txt','r') as account:
        Salt = account.readline().rstrip()
        data = account.read()
    
    match = False
    
    while not match:
        try:
            kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=Salt.encode(),
                        iterations=10000,
                    )
            
            password = getpass('Enter password: ')
            
            key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
            fer = Fernet(key)
            
            account_data = fer.decrypt(data.encode()).decode()
            
        except:
            print('Wrong password!')
            #clear_output(wait=True)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            match = True
    
    account_data = json.loads(account_data)
    
    return (account_data, Salt, password)