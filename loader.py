from aiogram import Bot, Dispatcher, types
from data import config
import quotes
import database

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)