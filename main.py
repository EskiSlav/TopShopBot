# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.
from constants import (
    LANG, LANG_CHOOSE_STATUS, NORMAL_STATUS, CATALOG_STATUS, IN_GAME, GAME_REQUEST
    ) 
from credentials import TOKEN
from database import DB

from keyboards import (
    ReplyKeyboard,
    InlineKeyboard
)
from pprint import pprint
import sqlite3              
import telebot
from telebot.types import ReplyKeyboardRemove

db = DB()
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'hello',
    reply_markup=InlineKeyboard.create_language_keyboard())
    db.add_user_bot(message)

@bot.message_handler(commands=['game'])
def start_game(message):
    db.update_status(message.chat.id, status=GAME_REQUEST)
    bot.send_message(message.chat.id, "Ого, ты решил поиграть в игру! Что же, рады тебя приветствовать, только сейчас мы проверим один нюанс ... \nНам нужен твой номер заказа, чтобы зарегестрировать в игре, не мог ты помочь и прислать его нам, а если у тебя его еще нету, то чего ты ждешь и покупай лучшую пижаму во всё СНГ!")



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'help')


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    db.update_language(user_id=call.from_user.id, language=call.data.split()[1])
    db.update_status(call.from_user.id, status=NORMAL_STATUS)
    lang = LANG[db.get_user_language(user_id=call.from_user.id)] # Get corresponding language
    bot.send_message(call.from_user.id, lang['language_changed'], reply_markup=ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'], func=lambda message: db.get_user_status(user_id=message.chat.id) == LANG_CHOOSE_STATUS)
def user_choosed_language(message):
    lang = None
    if   message.text == 'EN': lang = 'en'
    elif message.text == 'RU': lang = 'ru'
    elif message.text == 'UA': lang = 'ua'
    else:
        bot.send_message(message.chat.id, "Please, select some language below", ReplyKeyboard.generate_keyboard("EN", "RU", "UA"))
    db.update_language(user_id=message.chat.id, language=lang)
    db.update_status(user_id=message.chat.id, status=NORMAL_STATUS)


# handle messages when user does not have any status
@bot.message_handler(content_types=['text'])
def handle_normal_messages(message): 
    lang = LANG[db.get_user_language(user_id=message.chat.id)]
    text = message.text
    if text == lang['catalog']:
        db.update_status(user_id=message.chat.id, status=CATALOG_STATUS)

bot.polling(80)