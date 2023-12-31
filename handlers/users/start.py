from aiogram import types
from loader import dp
from loader import quotes, database
import keyboards
from data import fs_machine

VerifyStateGroup = fs_machine.VerifyStateGroup

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
	await message.answer(quotes.commands['start'])
	await message.answer(quotes.text['check_user'], reply_markup=keyboards.users.request_number)
	await VerifyStateGroup.number.set()