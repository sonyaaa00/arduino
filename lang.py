from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn2 = KeyboardButton('🇷🇺')
btn1 = KeyboardButton('🇬🇧')
lang = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2)
