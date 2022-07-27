import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


TOKEN = '5274991861:AAE994UxTFTIT-qDq6upcRTx2U1ltPKwxgc' #Токен бота
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN,parse_mode='html')
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)