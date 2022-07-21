from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.inline.group import group_inline_btn
from buttons.inline.subject import subject_inline_btn
from buttons.inline.teacher import teacher_inline_btn
from buttons.keyboard.group import GROUP_TEACHER_TEXT, group_markup
from db.dto import SubjectDTO, GroupDto, UserDto
from db.model_group import Group
from db.model_subject import Subject
from db.model_teacher import User
from dispacher import dp
from states.admin.group import GroupState
from states.admin.group_teacher_add import TeacherGroupState


@dp.message_handler(lambda message: str(message.text).__eq__(GROUP_TEACHER_TEXT), state=GroupState.crud_choice)
async def update_teacher_handler(message: types.Message):
    subjects: List[SubjectDTO] = Subject().select_all_subject()
    await TeacherGroupState.subject.set()
    await message.bot.send_message(chat_id=message.chat.id, text="Gurupani yo'nalishini tanlang 👇",
                                   reply_markup=subject_inline_btn(subjects))


@dp.callback_query_handler(state=TeacherGroupState.subject)
async def callback_subject_handler(callback: types.CallbackQuery, state=FSMContext):
    if callback.data == 'back':
        await callback.message.delete()
        await GroupState.crud_choice.set()
        await callback.message.answer(text='Tanlang', reply_markup=group_markup())
    else:
        async with state.proxy() as data:
            data['subject_id'] = int(callback.data)

        group: List[GroupDto] = Group().select_all_group(data.get('subject_id'))
        await callback.message.delete()
        await TeacherGroupState.group.set()
        await callback.message.bot.send_message(chat_id=callback.message.chat.id, text="Tanlang",
                                                reply_markup=group_inline_btn(group))


@dp.callback_query_handler(state=TeacherGroupState.group)
async def callback_delete_group_handler(callback: types.CallbackQuery, state=FSMContext):
    if callback.data == 'back':
        await callback.message.delete()
        subjects: List[SubjectDTO] = Subject().select_all_subject()
        await TeacherGroupState.subject.set()
        await callback.message.answer(text="Gurupani yo'nalishini tanlang 👇",
                                      reply_markup=subject_inline_btn(subjects))
    else:
        async with state.proxy() as data:
            data['group_id'] = callback.data
            data['chat_id'] = callback.message.chat.id
        await callback.message.delete()
        await TeacherGroupState.teacher.set()
        teachers: List[UserDto] = User().select_filter_teacher(data.get('subject_id'))
        await callback.message.answer(text='Birlashtiriladigan ustozni tanlang !',
                                      reply_markup=teacher_inline_btn(teachers))


@dp.callback_query_handler(state=TeacherGroupState.teacher)
async def callback_delete_group_handler(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
        pass
    if callback.data == 'back':
        group: List[GroupDto] = Group().select_all_group(data.get('subject_id'))
        await callback.message.delete()
        await TeacherGroupState.group.set()
        await callback.message.bot.send_message(chat_id=callback.message.chat.id, text="Tanlang",
                                                reply_markup=group_inline_btn(group))

    else:
        async with state.proxy() as data:
            data['teacher_id'] = callback.data
        await callback.message.delete()


        Group(subject_id=data.get('subject_id'),
              teacher_id=data.get('teacher_id'),
              create_by=data.get('chat_id'),
              _id=data.get('group_id')).update_group()
        await GroupState.crud_choice.set()
        await callback.message.answer(text = 'Tanlang' , reply_markup=group_markup())