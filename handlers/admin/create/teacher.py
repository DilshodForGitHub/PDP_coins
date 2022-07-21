from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.inline.auth import back_inline_markup
from buttons.inline.subject import subject_inline_btn
from buttons.keyboard.teacher import ADD_TEACHER_TEXT, teacher_markup, admin_teacher_markup
from db.dto import SubjectDTO
from db.enum import ROLE
from db.model_subject import Subject
from db.model_teacher import User
from dispacher import dp
from states.admin.teacher import AddTeacherState, TeacherState


@dp.message_handler(lambda message: str(message.text).__eq__(ADD_TEACHER_TEXT) , state=TeacherState.crud_choice)
async def subject_teacher_handler(message: types.Message):
    subjects: List[SubjectDTO] = Subject().select_all_subject()
    await AddTeacherState.subject.set()
    await message.bot.send_message(chat_id=message.chat.id , text = 'Qaysi fandan dars o\'tadi', reply_markup=subject_inline_btn(subjects))


@dp.callback_query_handler(state=AddTeacherState.subject)
async def callback_subject_handler(callback: types.CallbackQuery , state = FSMContext):
    if callback.data == 'back':
        await AddTeacherState.subject.set()

    async with state.proxy() as data:
        data['subject_id'] = callback.data
    await callback.message.delete()
    await AddTeacherState.phone.set()
    await callback.message.answer(text='Telefon nomer kiriting : ', reply_markup=back_inline_markup())




@dp.message_handler(state = AddTeacherState.phone)
async def teacher_handler(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        if len(message.text) <= 13:
            data['phone'] = message.text[1:]
            data['chat_id'] = message.chat.id
            response = User(phone_number=data.get('phone'),
                            subject_id=data.get('subject_id'),
                            role=ROLE.TEACHER.value,
                            created_by=int(data['chat_id'])).insert_user()
            if not response:
                await TeacherState.crud_choice.set()
                await message.bot.send_message(chat_id=message.chat.id, text='Successful',
                                               reply_markup=admin_teacher_markup())
            else:
                await TeacherState.crud_choice.set()
                await message.bot.send_message(chat_id=message.chat.id, text='Bunday o\'qtuvchi ro\'yhatdan o\'tilgan❌',
                                               reply_markup=teacher_markup())
        else:
            await AddTeacherState.phone.set()
            await message.answer(text = "Kechirasiz telefon nomer to'gri kiriting ! Yana urunib ko'ring")




