import logging
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from random import *

from app.db import Database
import app.trig
import app.keyboards as kb

router = Router()
logging.basicConfig(level=logging.INFO)

db = Database('database.db')


@router.message(CommandStart())
async def start(message: Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id, message.from_user.username)  
        await message.answer("<b>Привет, " + message.from_user.first_name + "! Это бот для повторения тригонометрических формул.</b> \n \n Данный бот находится на этапе активной разработки и в будущем планируется помогать не только с повторением тригонометрических формул! \n \n © Ярослав 11'И'", reply_markup=kb.main, parse_mode='HTML')
    user_id = message.from_user.id
    db.set_active(user_id, 1)

@router.message(Command("help"))
async def help(message: Message):
  await message.answer("Список формул будет пополнять в будущем с поступлением новых обновлений")
  await message.answer(f"Все формулы:\n{app.trig.help_text}", parse_mode='HTML')

