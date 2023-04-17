token = '5604892595:AAHtFecwz9fVrBKCF5g_B48vU-N-om-KUEc'
from aiogram import Bot , Dispatcher , types
from aiogram.utils import executor
from translator import tarjimon
bot = Bot(token=token)
db = Dispatcher(bot = bot)
@db.message_handler(commands='start')
async def start_command(message:types.Message):
    await message.answer('Iltimos yozing...')
@db.message_handler(content_types='text')
async def message_send(message:types.Message):
    text = message.text
    tarjima = tarjimon(text=text)
    await message.answer(tarjima)
if __name__ == '__main__':
    executor.start_polling(dispatcher=db)    

