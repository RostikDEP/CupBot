from aiogram.dispatcher.filters.state import State, StatesGroup

class VerifyStateGroup(StatesGroup):
	number = State()
	name = State()