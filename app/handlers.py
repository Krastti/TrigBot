import logging
from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from random import *

import app.trig
import app.keyboards as kb

router = Router()
logging.basicConfig(level=logging.INFO)

@router.message(CommandStart())
async def start(message: Message):
  await message.answer("Привет " + message.from_user.first_name + "! Это бот для повторения тригонометрических формул.\n \n Пожалуйста, перед использованием данного бота, ознакомьтесь с правильным написанием всех формул с помощью команды /help. Вы также можете выбрать количество вопросов в диктанте", reply_markup=kb.main)

@router.message(Command("help"))
async def help(message: Message):
  await message.answer("Данный бот пока что находится на этапе разработки и система ввода формул не настроена. Бот будет считывать только так, как ему заданно в массиве данных, поэтому прошу обращаться к нему в случае ошибки")
  data_string = "\n".join(app.trig.help_text)
  await message.answer(f"Все формулы:\n{data_string}")

user_game_data = {}
# Обработчик команды /game
@router.message(Command("game"))
async def start_game(message: types.Message):
    user_id = message.from_user.id

    # Если пользователь уже играет, предупреждаем
    if user_id in user_game_data:
        await message.reply("Вы уже начали игру. Чтобы остановить, введите /stop.")
        return

    # Инициализируем игру для пользователя
    user_game_data[user_id] = {
        "current_question": None,  # Текущий вопрос
        "correct_answer": None     # Правильный ответ
    }

    await ask_new_question(message)

# Функция для выбора нового вопроса и отправки его пользователю
async def ask_new_question(message: types.Message):
    user_id = message.from_user.id

    # Выбираем случайную формулу из массива
    question_data = choice(app.trig.formulas)
    user_game_data[user_id]['current_question'] = question_data['question']
    user_game_data[user_id]['correct_answer'] = question_data['answer']

    # Отправляем вопрос пользователю
    await message.reply(f"Решите: {question_data['question']}")

# Обработчик команды /stop
@router.message(Command('stop'))
async def stop_game(message: types.Message):
    user_id = message.from_user.id

    # Проверяем, если пользователь не играл
    if user_id not in user_game_data:
        await message.reply("Вы не начали игру. Чтобы начать, введите /game.")
        return

    # Удаляем данные пользователя
    del user_game_data[user_id]
    await message.reply("Игра остановлена.")

# Обработчик ответов на вопросы
@router.message(lambda message: message.from_user.id in user_game_data)
async def check_answer(message: types.Message):
    user_id = message.from_user.id
    user_data = user_game_data[user_id]
    correct_answer = user_data['correct_answer']

    # Проверка ответа
    if message.text == correct_answer:
        await message.reply("Правильно! Вот следующий вопрос.")
        await ask_new_question(message)
    else:
        await message.reply("Неправильно, попробуйте еще раз.")

