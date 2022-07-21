from aiogram.dispatcher.filters.state import StatesGroup, State


class GroupStudentState(StatesGroup):
    subject = State()
    group = State()
    fullname = State()
    phone = State()
