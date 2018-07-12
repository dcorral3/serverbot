#! /usr/bin/python3

import sys
import time
import telepot
import config
import commands
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
def auth(chat_id):
    return True
    # return chat_id == config.chat_id

def c_handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if auth(chat_id):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                       [InlineKeyboardButton(text='Hostname',
                           callback_data='hostname'),
                        InlineKeyboardButton(text='IP', callback_data='get_ip')]
                    ])
        bot.sendMessage(chat_id, 'Server menu:', reply_markup=keyboard)
        print(content_type, chat_type, chat_id)
    else:
        bot.sendMessage(chat_id, "Sorry, you don't have authorization")
def cb_handle(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    if auth(from_id):
        if query_data == 'hostname':
            res = commands.get_hostname()
        elif query_data == 'get_ip':
            res = commands.get_ip()
        else:
            print('Callback Query:', query_id, from_id, query_data)
            bot.answerCallbackQuery(query_id, text='Got it')
        bot.answerCallbackQuery(query_id, text=res)
        print(query_id, from_id, query_data)
    else:
        bot.sendMessage(chat_id, "Sorry, you don't have authorization")

TOKEN = config.TOKEN 

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'callback_query':cb_handle,'chat': c_handle}).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
