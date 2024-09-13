from aiogram import Router
from aiogram.filters import Command
import logging
from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from random import *

from app.db import Database
import app.keyboards as kb
import app.trig

router = Router()
logging.basicConfig(level=logging.INFO)

db = Database('database.db')

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

    # Генерация клавиатуры с правильными и неправильными ответами
    user_data = user_game_data[user_id]
    correct_answer = user_data['correct_answer']
    
    answers = [correct_answer]
    
    while len(answers) < 4:
        random_data = choice(app.trig.formulas)
        random_answer = random_data['answer']
        
        if random_answer not in answers:
            answers.append(random_answer)
    shuffle(answers)
    
    keyboardButton = []
    for i in range(0, len(answers), 2):
        row = []
        row.append(KeyboardButton(text=answers[i]))
        if (i + 1) < len(answers):
            row.append(KeyboardButton(text=answers[i+1]))
        keyboardButton.append(row)
    keyboardButton.append([KeyboardButton(text='/stop')])
    markup =ReplyKeyboardMarkup(keyboard=keyboardButton, resize_keyboard=True)
    await message.reply(f"Решите: {question_data['question']}", reply_markup=markup)


# Обработчик команды /stop
@router.message(Command('stop'))
async def stop_game(message: types.Message):
    user_id = message.from_user.id

    # Проверяем, если пользователь не играл
    if user_id not in user_game_data:
        await message.reply("Вы не начали игру. Чтобы начать, введите /game.", reply_markup=kb.main)
        return

    # Удаляем данные пользователя
    del user_game_data[user_id]
    await message.reply("Игра остановлена.", reply_markup=kb.main)

# Обработчик ответов пользователя
@router.message()
async def check_answer(message: types.Message):
    user_id = message.from_user.id
    
    # Проверяем, начал ли пользователь игру
    if user_id not in user_game_data:
        await message.reply("Пожалуйста, начните игру командой /game.")
        return

    # Проверяем ответ
    user_answer = message.text
    correct_answer = user_game_data[user_id]['correct_answer']
    
    if user_answer == correct_answer:
        await message.answer('Правильно! Вот следующий вопрос.')
        # Здесь можно вызвать функцию для нового вопроса
        await ask_new_question(message)
    else:
        await message.answer('Неправильно, попробуйте еще раз!')