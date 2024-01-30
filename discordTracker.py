import requests

def retrieve_messages(channelid):
    
    # Retrieve messages from a discord channel
    # send the messages retrieved to the print_messages() function.
    
    
    headers = {
        'authorization': '(put channel authorization here)',
        'X-RateLimit-Limit': '45',
        'X-RateLimit-Reset-After': '1'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)

            

        
    while True:
        time.sleep(1)
        jsonn = print_messages(channelid, jsonn)

                

def print_messages(channelid, jsonn):
    
    # Takes the messages from the same channel as the channel used for jsonn and puts it in checker 
    # if the top message id from checker isn't the same as the top message id from jsonn, then a new message was sent
    # if a new message was sent, prints it in the terminal with print_new_messages(), then send back checker.
    
    headers = {
        'authorization': '(put channel authorization here)',
        'X-RateLimit-Limit': '45',
        'X-RateLimit-Reset-After': '1'
    }

    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    checker = json.loads(r.text)
    # Get the top message ID from jsonn
    id1 = jsonn[0]['id'] if jsonn else None
    
    # Get the top message ID from checker
    id2 = checker[0]['id'] if checker else None
    
    # Compare top message IDs
    if id1 != id2:
        print_new_messages(checker)
    
    return checker

def print_new_messages(messages):
    for value in messages:
        print(f"Message from {value['author']['username']}:")
        print(value['content'], "\n")