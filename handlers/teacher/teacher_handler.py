from typing import List


from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.inline.subject import subject_inline_btn
from buttons.keyboard.teacher import teacher_phone_markup, teacher_markup
from db.dto import SubjectDTO
from db.enum import ROLE
from db.model_subject import Subject
from db.model_teacher import User
from dispacher import dp


from states.teacher import TeacherState





@dp.message_handler(commands='teacher')
async def admin_handler(message: types.Message):
    await TeacherState.phone_number.set()

    await message.answer(text='Berilgan tugmani bosib nomeriz jo\'nat'
                              'ing', reply_markup=teacher_phone_markup())

@dp.message_handler(content_types=types.ContentType.CONTACT,state=TeacherState.phone_number)
async def teacher_phone_handler(message: types.Message , state = FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number[1:]

    response = User(phone_number=data.get('phone_number')).phone_number_check(register=True)
    if not response:
        subject: List[SubjectDTO] = Subject().select_all_subject()
        await TeacherState.subject.set()
        await message.answer(text = "Dars o'tadigan fanizni tanlang : " ,reply_markup=subject_inline_btn(subject) )
    else:
        await TeacherState.teacher_menu_choice.set()
        await message.answer(text='tanlang', reply_markup=teacher_markup())


@dp.callback_query_handler(state=TeacherState.subject)
async def callback_subject_handler(callback: types.CallbackQuery,  state = FSMContext):
    async with state.proxy() as data:
        data['subject_id'] = callback.data
        data['chat_id'] = callback.message.chat.id

    await TeacherState.fullname.set()
    await callback.message.bot.send_message(chat_id=callback.message.chat.id , text="To'liq ism familyani kiriting ")

@dp.message_handler(state=TeacherState.fullname)
async def fullname_handler(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text
    await TeacherState.photo.set()
    await message.bot.send_message(chat_id=message.chat.id , text = 'Rasmizni junating : ')

@dp.message_handler(content_types=types.ContentType.PHOTO, state = TeacherState.photo)
async def photo_handler(message: types.Message , state = FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0]['file_id']
        data['role'] = ROLE.TEACHER.value

    await TeacherState.description.set()
    await message.answer(text= 'Oziz haqizda malumot qoldiring (Ish stajlari , sertifikat .....)')

@dp.message_handler(state=TeacherState.description)
async def description_handler(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text


    User(fullname=data.get('fullname') ,
         role = data.get('role'),
         phone_number=str(data.get('phone_number')),
         about=data.get('description'),
         photo=data.get('photo'),
         subject_id=data.get('subject_id'),
         chat_id=data.get('chat_id')).update_teacher()
    await TeacherState.teacher_menu_choice.set()
    await message.answer(text='tanlang', reply_markup=teacher_markup())






































