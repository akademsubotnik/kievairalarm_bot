from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6454077984:AAHqNy50ZKN-daZvmUYDr_Z2ymdBUmNk3bk'
BOT_USERNAME: Final = '@kievairalarm_bot'

async def start_command()