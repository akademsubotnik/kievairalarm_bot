""""main.py"""

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    #ContextTypes,

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


######
#MAIN#
######

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

#Job Queue
job_queue = app.job_queue
job_minute = job_queue.run_repeating(callback_minute, interval=5, first=10)

# #Polls the bot
# print('Polling...')
app.run_polling()
