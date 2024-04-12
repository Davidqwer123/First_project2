from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


user = ReplyKeyboardMarkup(keyboard=
                           [[KeyboardButton(text="Поділитися контактом",
                            request_contact=True)]], resize_keyboard=True, one_time_keyboard=True)

start_test = ReplyKeyboardMarkup(keyboard=
            [[KeyboardButton(text="Почати опитування",
             request_contact=True)]], resize_keyboard=True, one_time_keyboard=True)