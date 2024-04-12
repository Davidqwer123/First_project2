
from keyboards.default import user
from loader import dp
from aiogram import types
import aiogram
import requests
import asyncio
import asyncpg
import loader







@dp.message_handler(commands ="start")
async def bot_echo(message: types.Message):
    await message.answer("Привіт!\nВітаю вас в телеграм боті де ви можете підібрати під себе путівку за кордон\nДля почаку зареєструйтесь ", reply_markup=user)



