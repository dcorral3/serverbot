#!/bin/python3

import sys
import time
import telepot
import config
import commands 
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def c_handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Hostname',
                       callback_data='hostname'), 
                    InlineKeyboardButton(text='IP', callback_data='get_ip')]
               ])
    bot.sendMessage(chat_id, 'Server menu:', reply_markup=keyboard)

def cb_handle(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    if query_data == 'hostname':
        res = commands.get_hostname()
    elif query_data == 'get_ip':
        res = commands.get_ip()
    else:
        print('Callback Query:', query_id, from_id, query_data)
        bot.answerCallbackQuery(query_id, text='Got it')
    
    bot.answerCallbackQuery(query_id, text=res)



TOKEN = config.TOKEN  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'callback_query':cb_handle,'chat': c_handle}).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
