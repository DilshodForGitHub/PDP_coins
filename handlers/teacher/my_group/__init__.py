from typing import List

from aiogram import types

from buttons.inline.group import group_inline_btn
from buttons.keyboard.teacher import MY_GROUP_TEXT
from db.dto import UserDto, GroupDto
from db.model_group import Group
from db.model_teacher import User
from dispacher import dp
from states.teacher import TeacherState, TeacherForGroupState


@dp.message_handler(lambda message: str(message.text).__eq__(MY_GROUP_TEXT),state = TeacherState.teacher_menu_choice)
async def my_group_handler(message: types.Message):
    response: UserDto = User(chat_id=message.chat.id).select_chat_id()
    group: List[GroupDto] = Group(teacher_id=response._id).filter_group_teacher_id()
    await TeacherForGroupState.group.set()
    await message.bot.send_message(chat_id=message.chat.id , text = 'Sizning gurupalaringiz :' , reply_markup=group_inline_btn(group=group))

@dp.callback_query_handler(state = TeacherForGroupState.group)
async def callback_group_handler(callback: types.CallbackQuery):
    pass
