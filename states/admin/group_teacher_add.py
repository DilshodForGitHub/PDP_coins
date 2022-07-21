from aiogram.dispatcher.filters.state import StatesGroup, State


class TeacherGroupState(StatesGroup):
    subject = State()
    group = State()
    teacher = State()