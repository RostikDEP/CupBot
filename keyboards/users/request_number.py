from aiogram import types
import quotes

request_number = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
request_button = types.KeyboardButton(quotes.keyboard.buttons['request_contact'], request_contact=True)
request_number.add(request_button)