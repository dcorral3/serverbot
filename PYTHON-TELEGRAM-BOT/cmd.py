from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import socket
import requests
import json

keyboard = [[InlineKeyboardButton("Hostname", callback_data='hostname'),
             InlineKeyboardButton("IP", callback_data='ip')],
            [InlineKeyboardButton("Option 3", callback_data='3')]]
reply_markup = InlineKeyboardMarkup(keyboard)

def start(bot, update):
    update.message.reply_text('Please choose:', reply_markup=reply_markup)
def button(bot, update):
    query = update.callback_query
    if query.data == "hostname":
        res = hostname()
    elif query.data == "ip":
        res = ip()
    else:
        res = "default"

    bot.send_message(chat_id=query.message.chat_id, text=res)
    bot.answer_callback_query(query.id)

def hostname():
    return socket.gethostname()

def ip():
    res = requests.get('https://api.ipify.org?format=json')
    return json.loads(res.text)["ip"]
