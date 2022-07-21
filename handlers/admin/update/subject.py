from aiogram import types

from buttons.keyboard.subject import UPDATE_SUBJECT_TEXT
from dispacher import dp
from states.admin.subject import SubjectState


@dp.message_handler(lambda message: str(message.text).__eq__(UPDATE_SUBJECT_TEXT) , state= SubjectState.crud_choice)
async def update_subject_state(message: types.Message):
    pass