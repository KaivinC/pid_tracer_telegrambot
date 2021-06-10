from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler 
from telegram.ext import MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton 
from telegram.ext import MessageHandler, Filters 
import os
import sys
import subprocess

token = ""

updater = Updater(token=token, use_context=False)

updater.start_polling()

dispatcher = updater.dispatcher

def Check_pid_exist(name):
    pro=["ps aux | awk '{print $2}'"]
    ps = subprocess.Popen(pro,stdout=subprocess.PIPE,shell=True)
    try:
        response = subprocess.check_output(['grep',"-w", name], stdin=ps.stdout)
    except:
        response = ""
    return response

def start(bot, update):
    message = update.message
    chat = message['chat']
    update.message.reply_text(text='The pid you want to check is?')

def echo(bot, update):
    message = update.message
    text = message.text
    status = Check_pid_exist(text)
    if status == "":
        update.message.reply_text(text="The process is not exist")
    else:
        update.message.reply_text(text="The process is exist")


dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(MessageHandler(Filters.text, echo))