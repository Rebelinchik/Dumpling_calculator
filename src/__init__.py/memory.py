from aiogram.fsm.state import State, StatesGroup


class MemoryBot(StatesGroup):
    wait_res = State()
