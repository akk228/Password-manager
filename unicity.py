def is_unique (data, account_data):
    
    List_of_addresses = []
    
    for i in range(len(account_data)):
        if data['Website'] == account_data[i]['Website']:
            List_of_addresses.append(account_data[i])
    if len(List_of_addresses) == 0:
        return True
    
    for i in range(len(List_of_addresses)):
        if data['Login'] == List_of_addresses[i]['Login']:
            return False
        
    return True