def close_account (login, account_data, Salt, password):
    from getpass import getpass
    #from IPython.display import clear_output
    import json
    import base64
    import os
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    
    
    
    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=Salt.encode(),
                        iterations=10000,
                    )
    
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    fer = Fernet(key)
    token = fer.encrypt(b"Super secret message!")
    
    data = json.dumps(account_data)
    encrypted_data = fer.encrypt(data.encode())
    
    with open(login + '.txt','w') as file:
        file.write(Salt + '\n')
        file.write(encrypted_data.decode())