""""main.py"""

from telegram.ext import Application
from python_telegram_messager import (
    error,
    TOKEN,
    alarmcheck_minute
)
import logging


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
job_minute = job_queue.run_repeating(alarmcheck_minute, interval=60, first=10)

# #Polls the bot
# print('Polling...')
app.run_polling()
