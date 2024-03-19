
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
import menu as m
#from arduino2 import temperature, humidity
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
BOT_TOKEN = '6731888930:AAHnVFFX7U5VBakPkz4s00k-4o7h6t0Dcv8'
bot = Bot(token=BOT_TOKEN)
CHAT_ID = '6731888930'
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer('Привет! \n (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧', reply_markup= m.mainMenu)
    await message.answer('Это бот PlantPal - ваш помошник в уходе за растениями 🌱\n🔹PlantPal отправит данные о среде, окружающей растение. \n🔹Или построит графики по данным. \n🔹А ещё уведомит о критических значениях на датчиках, чтобы вы точно не забыли полить растение или включить подсветку для рассады. ', reply_markup= m.mainMenu)
    await bot.send_video(message.chat.id, open('plantpal.mp4', 'rb'))   
'''
@dp.message_handler()
async def message(message: types.Message):
    if message.text == 'Параметры окружающей среды ✅':
        await message.answer(f'Температура: {temperature}\n Влажность воздуха: {humidity}\n Влажность почвы:\n Интенсивность света:\n ', reply_markup=m.mainMenu)
    elif message.text == 'Графики 📊':
        await message.answer(message.from_user.id, 'Давайте построим график!', reply_markup=m.mainMenu)
        with open('tmp.png', 'rb') as photo_file:
            graph = types.InputFile(photo_file)
        await bot.send_photo(chat_id=CHAT_ID, photo=graph)
'''

    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
