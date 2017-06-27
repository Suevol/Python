# -*- coding: utf-8 -*-
#Bot name: EvgenySubbotenkoBot
#бот реагирует на упоменание о погоде и предлагает сообщить температуру в указанном городе
import telebot
from telebot import types
import time
import pyowm
import re

owm = pyowm.OWM('ваш валидный API ключ')
token = 'ваш валидный токен'
bot = telebot.TeleBot(token)

@bot.message_handler(regexp=r'\w\sпогод\w')
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Да, конечно!', 'Нет, спасибо']])
    msg = bot.send_message(message.chat.id, 'хотите узнать температуру воздуха в интересующем Вас городе?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, answer)

@bot.callback_query_handler(func=lambda message: message.data)
def answer(message):
    if message.text == 'Да, конечно!':
        bot.send_message(message.chat.id, 'укажите название города')
        @bot.message_handler(content_types=['text'])
        def weather(m):
            observation = owm.weather_at_place(m.text)
            w = observation.get_weather()
            temperature = w.get_temperature('celsius')['temp']
            answer_yes = ('В городе {0} в данный момент температура воздуха: {1}'.format(m.text, str(temperature)))
            bot.send_message(message.chat.id, answer_yes, parse_mode='Markdown')
    elif message.text == 'Нет, спасибо':
        bot.send_message(message.chat.id, 'Буду рад помочь Вам позже')
    else:
        bot.send_message(message.chat.id, 'Я Вас не понял, пожалуйста задайте Ваш вопрос еще раз')

if __name__ == '__main__':
    bot.polling(none_stop=True)