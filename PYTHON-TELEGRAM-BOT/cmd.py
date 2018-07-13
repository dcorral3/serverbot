from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import socket
import requests
import json
from config import DNS_pass, hosts

keyboard = [[InlineKeyboardButton("Hostname", callback_data='hostname'),
             InlineKeyboardButton("IP", callback_data='ip')],
            [InlineKeyboardButton("Update IP", callback_data='update_ip')]]
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
        res = update_ip()

    bot.send_message(chat_id=query.message.chat_id, text=res)
    bot.answer_callback_query(query.id)

def hostname():
    return socket.gethostname()

def ip():
    res = requests.get('https://api.ipify.org?format=json')
    return json.loads(res.text)["ip"]

def update_ip():
    res = ""
    for host in hosts:
        res_url = requests.get('https://dynamicdns.park-your-domain.com/update?host='+ host +'&domain=diegoct.com&password='+ DNS_pass +'&ip=')
        res = res + host +": " + str(res_url.status_code)+"\n"
    return res
