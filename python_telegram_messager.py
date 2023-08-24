"""module for telegram messager in python"""

from typing import Final
from telegram import Update
from telegram.ext import ContextTypes

#cp from thisis_kyiv to private telegram channel
from readpublicchannels.telethon_main import get_latestmessage

#air alarms
import asyncio
import nest_asyncio
from check_for_alarms import check_for_alarm

TOKEN: Final = '6454077984:AAHqNy50ZKN-daZvmUYDr_Z2ymdBUmNk3bk'
BOT_USERNAME: Final = '@kievairalarm_bot'

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
        str_alarm = "THERE IS AN AIR ALARM IN KIEV CITY!"
        #RUN THE TELETHON_MAIN FUNCTION!!!!!!
    if alarm == False:
        str_alarm = "there is no air alarm in kiev city"

    await context.bot.send_message(chat_id='@kcairalarm', text=str_alarm)
