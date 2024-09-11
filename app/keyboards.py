from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/help")],
                                     [KeyboardButton(text="/game")],
                                     [KeyboardButton(text="/stop")]],
                          resize_keyboard=True)