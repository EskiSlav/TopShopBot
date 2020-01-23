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
        keyboard.add()
        return keyboard

    @classmethod
    def generate_language_keyboard(cls):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('EN', 'RU', 'UA')



class InlineKeyboard(Keyboard):

    @classmethod
    def hello(cls):
        cls.keyboard.add(types.InlineKeyboardButton("FAQ"),types.InlineKeyboardButton("Каталог Каналов"))

    @classmethod
    def create_keyboard(cls, buttons:list, *args, **kwargs):
        keyboard = types.InlineKeyboardMarkup()
        buttons_ready = []
        for button in buttons:
            buttons_ready.append(types.InlineKeyboardButton(button[0], callback_data='lang ' +button[1]))
        keyboard.row(buttons_ready[0], buttons_ready[1], buttons_ready[2])
        return keyboard

    @classmethod
    def create_language_keyboard(cls):
        lst = [
                ('EN', 'en'),
                ('RU', 'ru'),
                ('UA', 'ua')
            ]
        return InlineKeyboard.create_keyboard(lst)


# class Test:
#     text = 'hello'

#     @classmethod
#     def ret(cls):
#         return cls.text.upper()
