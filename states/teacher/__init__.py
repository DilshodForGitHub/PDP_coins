from aiogram.dispatcher.filters.state import StatesGroup, State


class TeacherState(StatesGroup):
    phone_number = State()
    role = State()
    subject = State()
    fullname = State()
    photo = State()
    description = State()
    teacher_menu_choice = State()

class TeacherForGroupState(StatesGroup):
    group = State()



