#! /usr/bin/python3
from telegram import Bot
import requests
import json
from config import TOKEN, ip_file_path, admin_id
from cmd import ip, update_ip
bot = Bot(token=TOKEN)
file = open(ip_file_path, "r") 
pre_ip = file.read().rstrip()
file.close()
curr_ip = ip()
if curr_ip != pre_ip:
    file = open(ip_file_path, "w")
    file.write(curr_ip)
    file.close()
    bot.send_message(admin_id, "Your IP has changed:\nPre_IP: "+pre_ip+"\n"+"Curr_IP: "+curr_ip)
    update_ip()
