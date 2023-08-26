"""module for telegram messager in python"""

from typing import Final
from telegram import Update
from telegram.ext import ContextTypes

#cp from thisis_kyiv to private telegram channel
# from readpublicchannels.telethon_main import (
#     get_latestmessage,
#     API_HASH,
#     API_ID,
#     CLIENT,
# )

#air alarms
import asyncio
import nest_asyncio
from check_for_alarms import check_for_alarm

#telethon_main
import time
from telethon import TelegramClient
import aiohttp
import logging

# Remember to use your own values from my.telegram.org!
#telethon constss
API_ID: Final = 16451568
API_HASH: Final = '0e22fa1aaca1ef1bc7feba02f6f53622'
CLIENT: Final = TelegramClient('anon', API_ID, API_HASH)



#air alarm consts
TOKEN: Final = '6454077984:AAHqNy50ZKN-daZvmUYDr_Z2ymdBUmNk3bk'
BOT_USERNAME: Final = '@kievairalarm_bot'


async def get_latestmessage() -> str:
    """"Get latestmessage from public telegram channel"""
    #Code to get latest message from "thisis_kyiv" TG channel
    message = await CLIENT.get_messages('thisis_kyiv', 1)
    latest_message = message[0].text
    return latest_message

#errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """fnxn to handle errors"""
    print(f'Update {update} caused error {context.error}')

async def alarmcheck_minute(context: ContextTypes.DEFAULT_TYPE):
    """"fnxn to send messages to TG channel on timer"""
    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    alarm = loop.run_until_complete(asyncio.ensure_future(check_for_alarm()))
    if alarm == True:
        logging.warning("THERE IS AN AIR ALARM IN KIEV CITY!")
        async with CLIENT:
                latest_message = CLIENT.loop.run_until_complete(get_latestmessage())
        await context.bot.send_message(chat_id='@kcairalarm', text=latest_message) 
        #RUN THE TELETHON_MAIN FUNCTION!!!!!!
        #await get_latestmessage()    
    if alarm == False:
        logging.warning("there is no air alarm in kiev city")    


