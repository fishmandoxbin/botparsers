from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Кнопка для отправки телефона

markup = ReplyKeyboardMarkup(resize_keyboard=True)
phone = KeyboardButton("Отправить номер телефона", request_contact=True)
phone_kb = markup.add(phone)

# Меню для выбора чего-то

menu = [
    [InlineKeyboardButton("🔎 Начать поиска", callback_data='poisk')],
    [InlineKeyboardButton("⚙️Аккаунт", callback_data='account')],
    [InlineKeyboardButton("🆘 Помощь", callback_data='help')]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu, row_width=2)