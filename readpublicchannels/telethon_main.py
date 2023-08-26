from telethon import TelegramClient
import time
from typing import Final
import logging


# Remember to use your own values from my.telegram.org!
API_ID: Final = 16451568
API_HASH: Final = '0e22fa1aaca1ef1bc7feba02f6f53622'
CLIENT: Final = TelegramClient('anon', API_ID, API_HASH)
#logging.basicConfig(level=logging.DEBUG)


async def get_latestmessage():
    """"Get latestmessage from public telegram channel"""
    #Code to get latest message from "thisis_kyiv" TG channel
    previous_message = None
    while True:#while there is an air alarm run this
        message = await CLIENT.get_messages('air_alert_ua', 1)
        
        if message != previous_message:
            #logging.info("Value has changed!")
            print(f"{message[0].sender.username} {message[0].text}")# == print(message[0].sender.username + " " + message[0].text)
            #SEND TO PRIVATE TG CHANNEL 
        else:
            print("VED")
    
        previous_message = message
        time.sleep(5)
    

with CLIENT:
    CLIENT.loop.run_until_complete(get_latestmessage())
    
