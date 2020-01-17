from telebot import types

class Keyboard:
    keyboard = None


class ReplyKeyboard(Keyboard):
    
    @classmethod
    def generate_keyboard(cls, *args, **kwargs):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in args:
            keyboard.add(i)
        return keyboard

    @classmethod
    def hello(cls):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add("FAQ", "Каталог Товаров")
        return keyboard



class InlineKeyboard(Keyboard):

    @classmethod
    def generate_keyboard(cls, *args, **kwargs):
        keyboard = types.InlineKeyboardMarkup()
        for i in args:
            keyboard.add(types.InlineKeyboardButton(text=i, callback_data=i + "_Callback"))
        return keyboard

    @classmethod
    def hello(cls):
        cls.keyboard.add(types.InlineKeyboardButton("FAQ"),types.InlineKeyboardButton("Каталог Каналов"))




# class Test:
#     text = 'hello'

#     @classmethod
#     def ret(cls):
#         return cls.text.upper()
