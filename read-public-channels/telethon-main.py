from telethon import TelegramClient
import time

# Remember to use your own values from my.telegram.org!
api_id = 16451568
api_hash = '0e22fa1aaca1ef1bc7feba02f6f53622'
client = TelegramClient('anon', api_id, api_hash)


async def get_latestmessage():
    """"Get latestmessage from public telegram channel"""
    # You can print the message history of any chat:
    #this prints posts with latest post first
    #IDEA --- Get latest message and set it to a variable, every 5 seconds check if the message has chagned.  Is the message can changed set as the latest message and repeat!  
    #Code to get latest message from "thisis_kyiv" TG channel
    previous_message = None
    while True:#while there is an air alarm run this
        message = await client.get_messages('thisis_kyiv', 1)
        
        if message != previous_message:
            print("Value has changed!")
            actual_message = message[0].text
            actual_sender = message[0].sender.username
            print(actual_sender + " " + actual_message)
        else:
            print("VED")
    
        previous_message = message
        time.sleep(5)
    

with client:
    client.loop.run_until_complete(get_latestmessage())
    
