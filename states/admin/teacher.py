from aiogram.dispatcher.filters.state import StatesGroup, State


class TeacherState(StatesGroup):
    crud_choice = State()


class AddTeacherState(StatesGroup):
    subject  = State()
    phone = State()


class DeleteTeacherState(StatesGroup):
    delete_callback = State()


class UpdateTeacherState(StatesGroup):
    choice_teacher_callback = State()
    choice_fild_callback = State()
    new_value = State()
