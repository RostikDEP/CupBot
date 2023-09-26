from aiogram import types
from loader import dp

@dp.message_handler(text='/test')
async def command_start(message: types.Message):
	# await message.answer("Test")
	chat_id = message.chat.id
	first_name = message['from']['first_name']
	last_name = message['from']['last_name']
	