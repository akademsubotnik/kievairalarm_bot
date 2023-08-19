""""main.py"""
import asyncio
from check_for_alarms import check_for_alarm
#import python_telegram_messager

#while True:
asyncio.run(check_for_alarm())
