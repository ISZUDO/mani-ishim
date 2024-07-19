from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Birinchi tugma"),
            KeyboardButton(text="Ikkinchi tugma")
        ],
    ],
    resize_keyboard=True
)