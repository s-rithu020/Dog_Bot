
from telegram.ext import Updater, CommandHandler
import requests #getting data from cloud
import os

def get_url():
  contents = requests.get('https://random.dog/woof.json').json()
  url = contents['url']
  return url

def dog(bot,update):
  url = get_url()
  chat_id = update.message.chat_id
  bot.send_photo(chat_id,photo=url)

u = Updater('1032331580:AAFmatXB9N_uu0bXT6oaXSsaGJ04Jg_mItw')
dp = u.dispatcher
dp.add_handler(CommandHandler('dog',dog))
u.start_polling()
u.idle()
