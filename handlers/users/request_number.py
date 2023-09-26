from loader import dp
from database import users
import quotes
from data.fs_machine import VerifyStateGroup
from aiogram.dispatcher import FSMContext
from aiogram import types

@dp.message_handler(content_types=['contact'], state=VerifyStateGroup.number)
async def process_number(message, state: FSMContext):
	number = message.contact.phone_number
	is_exist = users.check_exits(str(number))

	if(is_exist):
		await message.answer(quotes.text['user_exist'])
		await state.finish()
	else:
		async with state.proxy() as data:
			data['number'] = str(number)

		await message.answer(quotes.text['user_not_exist'])
		await VerifyStateGroup.next()


@dp.message_handler(content_types=['text'], state=VerifyStateGroup.name)
async def get_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['username'] = message.text
		data['chat_id'] = message.chat.id
		data['first_name'] = message['from']['first_name']
		data['last_name']= message['from']['last_name']

		await message.answer(quotes.text['welcome_reg'].replace("0", data['username']))

		print(data)