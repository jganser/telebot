import time
import os
import random

import datetime

import parsedatetime

import telepot

from telepot.loop import MessageLoop

if not 'TELEGRAM_BOT_TOKEN' in os.environ:
   print('To use this docker image provide an valid value for the environment variable: TELEGRAM_BOT_TOKEN \n')
   print('You can add environment variables in the docker run command with the -e flag followed by the environment variable')
   print('Example: docker run -e TELEGRAM_BOT_TOKEN=<your-token> <this-image>')
   exit("No TELEGRAM_BOT_TOKEN found") 

def handle(msg):

   chat_id = msg['chat']['id']

   command = msg['text']

   print('Got command: %s' % command)

   print(chat_id)

   print(command)



   if command == '/roll':

       bot.sendMessage(chat_id, random.randint(1,6))

   elif command == '/time':

       bot.sendMessage(chat_id, str(datetime.datetime.now()))

   elif '/echo' in command:

       bot.sendMessage(chat_id, command[5:])

   elif '/chat_id' in command:

       bot.sendMessage(chat_id, chat_id)



bot = telepot.Bot(os.environ.get('TELEGRAM_BOT_TOKEN'))



MessageLoop(bot, handle).run_as_thread()

print('I am listening to {} ... '.format(os.environ.get('TELEGRAM_BOT_TOKEN')))




while 1:

    time.sleep(10)
