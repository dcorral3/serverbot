#!/usr/bin/python3
from config import TOKEN
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler , MessageHandler, Filters
import cmd
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', cmd.start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, cmd.echo)
dispatcher.add_handler(echo_handler)

button_handler = CallbackQueryHandler(cmd.button)
dispatcher.add_handler(button_handler)

updater.start_polling()

