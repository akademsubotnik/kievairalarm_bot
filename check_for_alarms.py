"""Module providingFunction to show air alarms in kiev city."""
import asyncio
import time
import aiohttp
from uasiren.client import Client


#run this is a while loop!
async def check_for_alarm():
    """Function to show air alarms in kiev city."""
    async with aiohttp.ClientSession() as session:
        
        client = Client(session)

        # All response formats are available here: https://api.ukrainealarm.com/swagger/index.html

        #kiev city is region 31
        region_alerts = await client.get_alerts(31)

        #we use the key 'activeAlerts' from the json we recieved to see if the number of AA is > 0
        if len(region_alerts[0]['activeAlerts']) > 0:
            str_alarm = "There is an alarm in kiev city"
            print(str_alarm.upper())
            #send message with telegram bot
        else:
            str_alarm = "There is no alarm in kiev city"
            print(str_alarm.lower())

        time.sleep(5)

#run indefinitly
#while True :
 #   asyncio.run(check_for_alarm())
    