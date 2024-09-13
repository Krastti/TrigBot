import logging
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message 

from app.db import Database
import app.keyboards as kb

class MyState(StatesGroup):
  message = State()

admin_router = Router()
logging.basicConfig(level=logging.INFO)

from main import Bot, admin_id
db = Database('database.db')

@admin_router.message(Command('admin'))
async def console(message: Message):
  user_id = message.from_user.id
  if message.chat.type == 'private' and user_id == admin_id:
    await message.answer('К вашим услугам', reply_markup=kb.admin_panel())

@admin_router.message(Command('list_user'))
async def list_user(message: Message):
    user_id = message.from_user.id
    users = db.get_users()
    if message.chat.type == 'private' and user_id == admin_id:
        for first_name in users:
            await message.answer(f'Список все пользователей {first_name}')

@admin_router.message(Command('send_all'))
async def send_all(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if message.chat.type == 'private' and user_id == admin_id:
        await message.answer('Напишите сообщение для рассылки')
        await state.set_state(MyState.message)

@admin_router.message(MyState.message)
async def test(message: Message, bot: Bot, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    users = db.get_users()
    if message.chat.type == 'private' and user_id == admin_id:
        success_count = 0
        fail_count = 0
        for user_id, active, first_name in users:
            if active:
                try:
                    await bot.send_message(chat_id=user_id, text=text)
                    success_count += 1
                except Exception as e:
                    await message.answer(f'Не удалось отправить сообщение {user_id}: {e}')
                    fail_count += 1
                    db.set_active(user_id, 0)
        await message.answer(f'Рассылка завершена. Успешно отправлено: {success_count}, ошибки {fail_count}')
        await state.clear()

@admin_router.message(Command('admin_stop'))
async def admin_stop(message: Message):
  await message.answer('Истинное наслаждение видеть вас за работой, сэр.', reply_markup=kb.main)