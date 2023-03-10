from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import decouple
from decouple import config

TOKEN = config('TOKEN')


bot = Bot(TOKEN)


db = Dispatcher(bot=bot)


@db.message_handler(commands=['start', 'hello', 'hi', 'hey', 'how are you?'])
async def start_handler(message: types.Message):
            await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}')
            await message.answer('что-то ещё?')


@db.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)
    await message.answer('что-то ещё?')
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
