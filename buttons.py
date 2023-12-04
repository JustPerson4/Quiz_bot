from telebot.types import KeyboardButton,ReplyKeyboardMarkup


def start_game():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button = KeyboardButton('share contact',request_contact=True)
    
    kb.add(button)
    return kb
    
def contact():
    kv = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button = KeyboardButton('play game')
    
    kv.add(button)
    return kv



    