from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
import menu as m
import lang as l
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
BOT_TOKEN = '6731888930:AAHnVFFX7U5VBakPkz4s00k-4o7h6t0Dcv8'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer('Привет!', reply_markup= m.mainMenu)
        

@dp.message_handler()
async def message(message: types.Message):
    if message.text == 'Параметры окружающей среды ✅':
        await message.answer(message.from_user.id, 'Температура:\n Влажность воздуха:\n Влажность почвы:\n Освещённость:\n ', reply_markup=m.mainMenu)
    elif message.text == 'Графики 📊':
        await message.answer(message.from_user.id, 'Давайте построим график!', reply_markup=m.mainMenu)
        await message.answer(message.from_user.id, 'Давайте построим график!', reply_markup=m.mainMenu)
        photo = InputFile("files/test.png")




    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)