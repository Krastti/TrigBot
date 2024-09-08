from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/help")],
                                     [KeyboardButton(text="/game")],
                                     [KeyboardButton(text="/stop")]],
                          resize_keyboard=True)

dictation = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="10 вопросов", callback_data="ten_question")],
                                                  [InlineKeyboardButton(text="15 вопросов", callback_data="fifteen_question")],
                                                  [InlineKeyboardButton(text="20 вопросов", callback_data="twente_question")],])