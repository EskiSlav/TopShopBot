import telebot
import sqlite3
from constants import PHRASES
from credentials import TOKEN
from keyboards import (
    ReplyKeyboard,
    InlineKeyboard
)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, PHRASES['hello'],
    reply_markup=ReplyKeyboard.generate_keyboard("FAQ", "Каталог"))


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, PHRASES['help'])


@bot.message_handler(content_types=['text'])
def handle(message):
    pass

bot.polling(80)