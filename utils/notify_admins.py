from data.config import ADMINS
from loader import dp

async def notify_admins(message):
	for admin in ADMINS:
		await dp.bot.send_message(admin, message)