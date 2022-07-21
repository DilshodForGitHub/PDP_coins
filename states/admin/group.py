from aiogram.dispatcher.filters.state import StatesGroup, State


class GroupState(StatesGroup):
    crud_choice = State()

class AddGroupState(StatesGroup):
    choice_subject = State()
    name = State()

class DeleteGroupState(StatesGroup):
    choice_subject = State()
    delete_callback = State()
