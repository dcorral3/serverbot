#!/usr/bin/python3
from config import TOKEN2
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import cmd
updater = Updater(token=TOKEN2)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', cmd.start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, cmd.echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
