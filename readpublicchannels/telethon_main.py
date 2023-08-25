from telethon import TelegramClient
import time
from typing import Final

# Remember to use your own values from my.telegram.org!
API_ID: Final = 16451568
API_HASH: Final = '0e22fa1aaca1ef1bc7feba02f6f53622'
CLIENT: Final = TelegramClient('anon', API_ID, API_HASH)


async def get_latestmessage():
    """"Get latestmessage from public telegram channel"""
    # You can print the message history of any chat:
    #this prints posts with latest post first
    #IDEA --- Get latest message and set it to a variable, every 5 seconds check if the message has chagned.  Is the message can changed set as the latest message and repeat!  
    #Code to get latest message from "thisis_kyiv" TG channel
    previous_message = None
    while True:#while there is an air alarm run this
        message = await CLIENT.get_messages('thisis_kyiv', 1)
        
        if message != previous_message:
            print("Value has changed!")
            print(f"{message[0].sender.username} {message[0].text}")# == print(message[0].sender.username + " " + message[0].text)
            #SEND TO PRIVATE TG CHANNEL 
        else:
            print("VED")
    
        previous_message = message
        time.sleep(5)
    

#with CLIENT:
#    CLIENT.loop.run_until_complete(get_latestmessage())
    
