import requests
import json
import time

"""
This program takes messages from a discord channel and keep tracks of new messages by printing it onto the user's terminal.
"""

def retrieve_messages(channelid):
    
    """
    Retrieve messages from a discord channel
    send the messages retrieved to the print_messages() function.
    """
    
    headers = {
        'authorization': 'put your channel authorization here',
        'X-RateLimit-Limit': '45',
        'X-RateLimit-Reset-After': '1'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)

            

        
    while True:
        time.sleep(1)
        jsonn = print_messages(channelid, jsonn)

                

def print_messages(channelid, jsonn):
    
    """
    Takes the messages from the same channel as the channel used for jsonn and puts it in checker 
    if the top message id from checker isn't the same as the top message id from jsonn, then a new message was sent
    if a new message was sent, prints it in the terminal, then send back checker.
    """

    headers = {
        'authorization': 'put your channel authorization here',
        'X-RateLimit-Limit': '45',
        'X-RateLimit-Reset-After': '1'
    }

    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    checker = json.loads(r.text)
    k = 0
    id1 = 0
    id2 = 0
    for value in checker:
        if k == 0:
            id1 = value['id']
            k += 1
        else:
            k = 0
            break
    for value in jsonn:
        if k == 0:
            id2 = value['id'] 
            k += 1
        else:
            k=0
            break
    if id1 != id2:
        for value in checker:
            if k == 0:
                print(f"Message from {value['author']['username']}:")      
                print(value['content'], "\n") 
                k += 1
            else:
                break
    return checker




retrieve_messages("put channel id here")