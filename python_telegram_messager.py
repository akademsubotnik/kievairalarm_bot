from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

#air alarms
import asyncio
from check_for_alarms import check_for_alarm

TOKEN: Final = '6454077984:AAHqNy50ZKN-daZvmUYDr_Z2ymdBUmNk3bk'
BOT_USERNAME: Final = '@kievairalarm_bot'

#errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am a kiev air alarm bot!')
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Please type something so that I can respond')
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! This is a custom command')    

#responses
def handle_response(text: str) -> str:
    processed: str = text.lower()   
    if 'hello' in processed:
        return 'Hey there!' 
    if 'how are you' in processed:
        return 'I am good thank you!'
    if 'i love python' in processed:
        return 'Remember to subscribe!'
    return 'I do not understand what you wrote...'

#handle message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)

