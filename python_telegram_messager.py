"""module for telegram messager in python"""

from typing import Final
from telegram import Update
from telegram.ext import ContextTypes


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

#commands
# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """fnxn when /start is typed"""
#     await update.message.reply_text('Hello! Thanks for chatting with me! I am a kiev air alarm bot!')
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """fnxn when /help is typed"""
#     await update.message.reply_text('Hello! Please type something so that I can respond')
# async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """fnxn when /custom is typed"""
#     await update.message.reply_text('Hello! This is a custom command')


#handle message
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """fnxn to handle message from user"""

#     nest_asyncio.apply()
#     loop = asyncio.get_event_loop()
#     alarm = loop.run_until_complete(asyncio.ensure_future(check_for_alarm()))
#     if alarm == True:
#         await update.message.reply_text("THERE IS AN AIR ALARM IN KIEV CITY!")
#     if alarm == False:
#         await update.message.reply_text("there is no air alarm in kiev city")


async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
    """"fnxn to send messages to TG channel on timer"""
    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    alarm = loop.run_until_complete(asyncio.ensure_future(check_for_alarm()))
    if alarm == True:
        str_alarm = "THERE IS AN AIR ALARM IN KIEV CITY!"
    if alarm == False:
        str_alarm = "there is no air alarm in kiev city"

    await context.bot.send_message(chat_id='@kcairalarm', text=str_alarm)