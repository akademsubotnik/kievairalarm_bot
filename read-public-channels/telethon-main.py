from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
api_id = 16451568
api_hash = '0e22fa1aaca1ef1bc7feba02f6f53622'
client = TelegramClient('anon', api_id, api_hash)



async def get_latestmessage():
    # You can print the message history of any chat:
    #this prints posts with latest post first
    #IDEA --- Get latest message and set it to a variable, every 5 seconds check if the message has chagned.  Is the message can changed set as the latest message and repeat!
    async for message in client.iter_messages('thisis_kyiv'):
        print(message.sender.username, message.text)

with client:
    client.loop.run_until_complete(get_latestmessage())