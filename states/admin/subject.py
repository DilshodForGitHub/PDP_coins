

# SUBJECT
from aiogram.dispatcher.filters.state import StatesGroup, State


class SubjectState(StatesGroup):
    crud_choice = State()

class AddSubjectState(StatesGroup):
    name = State()

class DeleteSubjectState(StatesGroup):
    delete_callback = State()