# kievairalarm_bot

TODO: Docker build is failing on pycairo after adding additional modules for passsing on messages to private channels

This is the code for a telegram bot that will alert when there is an air alarm in Kiev city

The bot is available at @kievairalarm_bot

To get air alarms in Kiev: 
  this project uses the uasiren python package, https://pypi.org/project/uasiren/

To send messages to telegram with python code:
  this project uses the python-telegram-bot python package, https://pypi.org/project/python-telegram-bot/


Code works, just need to work on self hosting...

#Future features, to include type of air alarm and a snippet of news regarding the reason for air alarm

I followed this to create a reproducible python file and docker images https://docs.docker.com/language/python/build-images/
