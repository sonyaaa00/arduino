from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnParams = KeyboardButton('Параметры окружающей среды ✅')
btnGraphics = KeyboardButton('Графики 📊')
btnLightOn = KeyboardButton('Освещение')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnParams, btnGraphics, btnLightOn)


