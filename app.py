import asyncio

async def on_startup(dp):
	from utils import set_default_commands
	await set_default_commands(dp)

	print("Bot is running")


if __name__ == "__main__":
	from aiogram import executor
	from handlers import dp

	executor.start_polling(dp, on_startup=on_startup)