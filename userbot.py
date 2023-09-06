from aiogram import Dispatcher, Bot, executor, types
import logging
import menuuserbot as kb
from aiogram.dispatcher.filters import Text
import textuser as txt
from aiogram.types import ReplyKeyboardRemove



token = '6656117885:AAFjxZVJJ9X1PfUlJdKEcjcAIv6tennyoDw'
bot = Bot(token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    messeges = '''
    Здравствуй <b>{user}</b>! Добро пожаловать в поисковую систему!
    '''.format(user=message.from_user.full_name)
    await message.answer(messeges, parse_mode='html')
    messages2 = '''🗂 <b>Номер телефона</b>
     
Вам необходимо подтвердить номер телефона для того, чтобы завершить индетификацию. 
     
<b>Для этого нажмите кнопку ниже.</b>'''
    await message.answer(messages2, parse_mode='html', reply_markup=kb.phone_kb)


@dp.message_handler(content_types='contact')
async def contact(message: types.Message):
    print("{user}".format(user=message.from_user.full_name))
    print("Телефон - {phone}".format(phone=message.contact.phone_number))
    await message.reply("<b>Ваш номер подтверждён успешно!</b>", parse_mode='html', reply_markup=ReplyKeyboardRemove())
    await message.answer("<b>Выберите нужное действие</b>", reply_markup=kb.menu, parse_mode='html')



@dp.callback_query_handler(text='poisk')
async def message_poisk(callback: types.CallbackQuery):
    await callback.message.answer(txt.text)
    await callback.message.edit_reply_markup()









if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)