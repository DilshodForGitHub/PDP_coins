from aiogram import types

from buttons.inline.auth import BACK_TEXT
from buttons.keyboard.auth import admin_markup
from buttons.keyboard.group import GROUP_TEXT, group_markup
from buttons.keyboard.subject import SUBJECT_TEXT, subject_markup
from buttons.keyboard.teacher import TEACHER_TEXT, admin_teacher_markup
from dispacher import dp
from states import AdminState
from states.admin.group import GroupState
from states.admin.subject import SubjectState
from states.admin.teacher import TeacherState


@dp.message_handler(commands='admin')
async def admin_handler(message: types.Message):
    await AdminState.menu_choice.set()
    await message.answer(text='Tanla', reply_markup=admin_markup())


# TEACHER
@dp.message_handler(lambda message: str(message.text).__eq__(TEACHER_TEXT), state=AdminState.menu_choice)
async def subject_handler(message: types.Message):
    await TeacherState.crud_choice.set()
    await message.answer(text='Tanlang', reply_markup=admin_teacher_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=TeacherState.crud_choice)
async def back_handler(message: types.Message):
    await AdminState.menu_choice.set()
    await message.answer(text='Tanla', reply_markup=admin_markup())


# SUBJECT
@dp.message_handler(lambda message: str(message.text).__eq__(SUBJECT_TEXT), state=AdminState.menu_choice)
async def subject_handler(message: types.Message):
    await SubjectState.crud_choice.set()
    await message.answer(text='Tanlang', reply_markup=subject_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=SubjectState.crud_choice)
async def back_handler(message: types.Message):
    await AdminState.menu_choice.set()
    await message.answer(text='Tanla', reply_markup=admin_markup())



# GROUP

@dp.message_handler(lambda message: str(message.text).__eq__(GROUP_TEXT), state=AdminState.menu_choice)
async def group_handler(message: types.Message):
    await GroupState.crud_choice.set()
    await message.answer(text='Tanlang', reply_markup=group_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=GroupState.crud_choice)
async def back_handler(message: types.Message):
    await AdminState.menu_choice.set()
    await message.answer(text='Tanla', reply_markup=admin_markup())
