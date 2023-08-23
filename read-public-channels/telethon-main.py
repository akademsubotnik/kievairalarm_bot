from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    # You can print the message history of any chat:
    async for message in client.iter_messages('USERNAME OF THE CHANNEL'):
        print(message.sender.username, message.text)

with client:
    client.loop.run_until_complete(main())