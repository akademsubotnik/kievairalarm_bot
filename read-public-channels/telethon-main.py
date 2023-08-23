from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
api_id = 16451568
api_hash = '0e22fa1aaca1ef1bc7feba02f6f53622'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    # You can print the message history of any chat:
    async for message in client.iter_messages('air_alert_ua'):
        print(message.sender.username, message.text)

with client:
    client.loop.run_until_complete(main())