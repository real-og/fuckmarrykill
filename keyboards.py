from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

proceed = KeyboardButton('Далее')
next = KeyboardButton('Следующий')
start = KeyboardButton('Играть')
end = KeyboardButton('Закончить')
add = KeyboardButton('Дополнить')

proceed_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).insert(proceed)
next_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).insert(next).row(end, add)
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).insert(start)




