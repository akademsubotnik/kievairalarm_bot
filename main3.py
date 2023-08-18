import asyncio
import aiohttp
from uasiren.client import Client


async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session)

        # All response formats are available here: https://api.ukrainealarm.com/swagger/index.html

        region_alerts = await client.get_alerts(31)
        print("alerts of region 31 (м. київ)", region_alerts)

        last_alert_index = await client.get_last_alert_index()
        print("last alert index", last_alert_index)

asyncio.run(main())