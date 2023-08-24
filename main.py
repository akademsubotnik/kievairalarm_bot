""""main.py"""

from telegram.ext import Application
from readpublicchannels.telethon_main import get_latestmessage
from python_telegram_messager import (
    error,
    TOKEN,
    callback_minute
)


######
#MAIN#
######

#PYTHON TELEGRAM MESSAGER
print('Starting the bot...')
app = Application.builder().token(TOKEN).build()

#Errors
app.add_error_handler(error)

#Job Queue
job_queue = app.job_queue
job_minute = job_queue.run_repeating(callback_minute, interval=60, first=10)

# #Polls the bot
# print('Polling...')
app.run_polling()
