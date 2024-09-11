import logging
from aiogram import Router, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from random import *

import app.trig
import app.keyboards as kb

router = Router()
logging.basicConfig(level=logging.INFO)

@router.message(CommandStart())
async def start(message: Message):
  await message.answer("<b>Привет, " + message.from_user.first_name + "! Это бот для повторения тригонометрических формул.</b> \n \n Пожалуйста, перед использованием данного бота, ознакомьтесь с правильным написанием всех формул с помощью команды /help.", reply_markup=kb.main, parse_mode='HTML')

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

    # Генерация клавиатуры с правильными и неправильными ответами
    user_data = user_game_data[user_id]
    correct_answer = user_data['correct_answer']
    
    random_data = choice(app.trig.formulas)
    random_data_2 = choice(app.trig.formulas)
    random_data_3 = choice(app.trig.formulas)
    
    random_answer = random_data['answer'] 
    random_answer_2 = random_data_2['answer']
    random_answer_3 = random_data_3['answer'] 
    
    if random_answer == correct_answer:
        random_answer = random_data['answer']
    if random_answer_2 == correct_answer:
        random_answer_2 = random_data_2['answer']
    if random_answer_3 == correct_answer:
        random_answer_3 = random_data_3['answer']
    
    markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f"{correct_answer}"), KeyboardButton(text=f"{random_answer}")],
                                            [KeyboardButton(text=f"{random_answer_2}"), KeyboardButton(text=f"{random_answer_3}")],
                                            [KeyboardButton(text='/stop')]], resize_keyboard=True)
    
    markup_2 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f"{random_answer}"), KeyboardButton(text=f"{correct_answer}")],
                                            [KeyboardButton(text=f"{random_answer_2}"), KeyboardButton(text=f"{random_answer_3}")],
                                            [KeyboardButton(text='/stop')]], resize_keyboard=True)
    
    markup_3 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f"{random_answer}"), KeyboardButton(text=f"{random_answer_2}")],
                                            [KeyboardButton(text=f"{correct_answer}"), KeyboardButton(text=f"{random_answer_3}")],
                                            [KeyboardButton(text='/stop')]], resize_keyboard=True)
    
    markup_4 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f"{random_answer}"), KeyboardButton(text=f"{random_answer_2}")],
                                            [KeyboardButton(text=f"{random_answer_3}"), KeyboardButton(text=f"{correct_answer}")],
                                            [KeyboardButton(text='/stop')]], resize_keyboard=True)
    
    markup_list = [markup, markup_2, markup_3, markup_4]
    # Отправляем вопрос пользователю
    await message.reply(f"Решите: {question_data['question']}", reply_markup=choice(markup_list))

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