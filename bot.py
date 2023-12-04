import telebot

import database

import buttons
from telebot.types import ReplyKeyboardMarkup,KeyboardButton



TOKEN = ('6535978716:AAFYdNjmhM3ojJviCukt9IHbffw0cnVETXc')

bot = telebot.TeleBot(TOKEN)

user_answers = {}

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.from_user.id, 'Salom!')
    
    

    
questions = [
    {
        "question": "Сколько типов данных есть в Python?",
        "options": ["3", "7", "4", "1"],
        "correct_option": 1,
    },
    {
        "question": "Какая столица Франции?",
        "options": ["Париж", "Лондон", "Берлин", "Рим"],
        "correct_option": 1,
    },
    {
        "question": "Кто является президентом США?",
        "options": ["Джо Байден", "Дональд Трамп", "Барак Обама", "Джордж Буш-младший"],
        "correct_option": 1,
    },
    {
        "question": "Какая столица Казахстана?",
        "options": ["Алматы", "Нур-Султан", "Астана", "Шымкент"],
        "correct_option": 1,
    },
    {
        "question": "Какая площадь поверхности Земли?",
        "options": ["510 миллионов квадратных километров", "510 тысяч квадратных километров", "510 миллиардов квадратных километров", "510 гектаров"],
        "correct_option": 1,
    },
    {
        "question": "Какая скорость света?",
        "options": ["299 792 458 метров в секунду", "299 792 458 километров в секунду", "299 792 458 километров в час", "299 792 458 миль в час"],
        "correct_option": 1,
    },
    {
        "question": "Какое самое большое число, которое можно выразить в виде 10^n?",
        "options": ["10^10", "10^100", "10^1000", "10^∞"],
        "correct_option": 1,
    },
    {
        "question": "Какое название имеет самая большая пустыня в мире?",
        "options": ["Сахара", "Австралийская пустыня", "Тайга", "Гоби"],
        "correct_option": 1,
    },
    {
        "question": "Какое название имеет самая высокая гора в мире?",
        "options": ["Эверест", "К2", "Канченджанга", "Лхоцзе"],
        "correct_option": 1,
    },
]

@bot.message_handler(commands=['start'])
def start_message(message):
   checker = database.check_user(message.from_user.id)
   
   if checker:
       bot.send_message(message.from_user.id, 'TO START GAME PRESS THE BUTTON',reply_markup=buttons.contact())# start knopka
   else:
       bot.send_message(message.from_user.id, 'share your contact to play game',reply_markup=buttons.start_game())# contact knopka
       bot.register_next_step_handler(message,get_contact)
       
def get_contact(message):
    if message.contact:
        user_phone = message.contact.phone_number
        first_name = message.contact.first_name
        
        database.register_user(first_name, message.from_user.id, user_phone)
        
        bot.send_message(message.from_user.id, 'You registered succesfully',reply_markup=buttons.contact())# start knopka

    else:
        bot.send_message(message.from_user.id, 'Pls to share button',reply_markup=buttons.start_game())# contact knopka
        bot.register_next_step_handler(message,get_contact)
        

@bot.message_handler(content_types=['text'])
def start_game(message):
  if message.text.lower() == 'play game':
    
    user_answers[message.from_user.id] = []
    start_the_game(message,message.from_user.id, 0)
   
def start_the_game(message,telegram_id,question_index):
  if question_index < len(questions):
    question_data = questions[question_index]
    question_text = question_data['question']
    question_options = question_data['options']
    
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True)
    
    for option in question_options:
      mark_up.add(KeyboardButton(option))
      
    bot.send_message(telegram_id,question_text, reply_markup=mark_up)
    bot.register_next_step_handler(message,is_correct_answer,telegram_id,question_data) 
    
  else:
      result = user_answers[telegram_id].count(True)
      
      bot.send_message(telegram_id, f'Your result is {len(questions)}/{result} correct')
        
            


    
def is_correct_answer(message, telegram_id, question_data):
  user_answer = message.text
  correct_answer = question_data['correct_option']

  if user_answer == question_data['options'][correct_answer]:
      user_answers[telegram_id].append(True)
    
  else:
    user_answers[telegram_id].append(False)
   
  next_question_index = len(user_answers[telegram_id])
  start_the_game(message,telegram_id,next_question_index)
    


    


bot.polling()