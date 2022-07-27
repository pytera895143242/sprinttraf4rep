from aiogram import types
from misc import dp,bot
from .sqlit import reg_user
from .callbak_data import st
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

content_chat = -1001523112454
ids_user = []

markup = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='12-17', callback_data='go_12')
bat_b = types.InlineKeyboardButton(text='18+', callback_data='go_18')
markup.add(bat_a, bat_b)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    reg_user(message.chat.id)
    await message.answer(text= "Привет, сколько тебе лет?",reply_markup=markup)


