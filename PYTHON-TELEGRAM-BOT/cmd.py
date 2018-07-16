from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import socket
import os
import requests
import json
from config import DNS_pass, hosts, admin_id

keyboard = [[InlineKeyboardButton("Hostname", callback_data='hostname'),
             InlineKeyboardButton("IP", callback_data='ip')],
            [InlineKeyboardButton("Update IP", callback_data='update_ip'),
             InlineKeyboardButton("Reboot", callback_data='reboot')]]
reply_markup = InlineKeyboardMarkup(keyboard)

def start(bot, update):
    update.message.reply_text('Please choose:', reply_markup=reply_markup)
def button(bot, update):
    query = update.callback_query
    if query.data == "hostname":
        res = hostname()
    elif query.data == "ip":
        res = ip()
    elif query.data == "update_ip":
        res = update_ip()
    elif query.data == "reboot":
        res = reboot(query.message.chat_id)
    else:
        print("nothing to do")

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

def reboot(chat_id):
    if str(chat_id) == admin_id:
        os.system("sudo reboot")
        return "reboot..."
    else:
        return "You are not authorized to do a reboot"
