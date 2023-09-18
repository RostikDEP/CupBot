from aiogram import types
from loader import dp
from loader import quotes

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
	await message.answer(quotes.commands['start'])