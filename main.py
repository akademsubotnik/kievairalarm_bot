""""main.py"""
#python messager
from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    JobQueue,

)
from python_telegram_messager import (
    start_command,
    help_command,
    custom_command,
    handle_message,
    error,
    TOKEN,
    callback_minute
)

#air alarms
import asyncio
from check_for_alarms import check_for_alarm

#import time
import time

######
#MAIN#
######

#ALARM CODE
#while True:
#asyncio.run(check_for_alarm())

#PYTHON TELEGRAM MESSAGER
print('Starting the bot...')
app = Application.builder().token(TOKEN).build()
#Commands
app.add_handler(CommandHandler('start', start_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('custom', custom_command))
#Messages
app.add_handler(MessageHandler(filters.TEXT, handle_message))
#Errors
app.add_error_handler(error)
# #Polls the bot
# print('Polling...')
# app.run_polling(poll_interval=3)
#Job Queue
job_queue = app.job_queue
job_minute = job_queue.run_repeating(callback_minute, interval=60, first=10)

app.run_polling()

# while True:

#     time.sleep(5)

