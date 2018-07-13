#!/usr/bin/python3
from config import TOKEN, admin_id
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler , MessageHandler, Filters
import cmd
import sys


updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

if len(sys.argv) > 1 and sys.argv[1]=="-r":
    updater.bot.send_message(chat_id=admin_id, text="Reboot performed")

start_handler = CommandHandler('start', cmd.start)
dispatcher.add_handler(start_handler)

button_handler = CallbackQueryHandler(cmd.button)
dispatcher.add_handler(button_handler)

updater.start_polling()

