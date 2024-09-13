from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/help")],
                                     [KeyboardButton(text="/game")],
                                     [KeyboardButton(text="/stop")]],
                          resize_keyboard=True)

def admin_panel() -> ReplyKeyboardMarkup:
  kb = ReplyKeyboardBuilder()
  kb.button(text='/send_all')
  kb.button(text='/list_user')
  kb.button(text='/admin_stop')
  kb.adjust(2)
  return kb.as_markup(resize_keyboard=True)