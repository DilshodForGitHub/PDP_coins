from aiogram import types

from buttons.keyboard.group import UPDATE_GROUP_TEXT
from dispacher import dp
from states.admin.group import GroupState


@dp.message_handler(lambda message: str(message.text).__eq__(UPDATE_GROUP_TEXT), state=GroupState.crud_choice)
async def update_group_handler(message: types.Message):
    pass
