from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.inline.teacher import teacher_inline_btn, teacher_fild_btn
from buttons.keyboard.teacher import UPDATE_TEACHER_TEXT, teacher_markup
from db.dto import UserDto
from db.model_teacher import User
from dispacher import dp
from states.admin.teacher import TeacherState, UpdateTeacherState


@dp.message_handler(lambda message: str(message.text).__eq__(UPDATE_TEACHER_TEXT), state=TeacherState.crud_choice)
async def update_teacher_handler(message: types.Message):
    teacher: List[UserDto] = User().select_all_teacher()
    await UpdateTeacherState.choice_teacher_callback.set()
    await message.bot.send_message(chat_id=message.chat.id, text='O\'qtuvchilar ro\'yhati',
                                   reply_markup=teacher_inline_btn(teacher))

@dp.message_handler(state=UpdateTeacherState.choice_teacher_callback)
async def delete_text_handler(message: types.Message):
    await message.delete()

@dp.callback_query_handler(state=UpdateTeacherState.choice_teacher_callback)
async def callback_query_for_subject(callback: types.CallbackQuery , state = FSMContext):
    if callback.data =='back':
        await callback.message.delete()
        await TeacherState.crud_choice.set()
        await callback.message.answer(text='Tanlang', reply_markup=teacher_markup())
    else:
        async with state.proxy() as data:
            data['teacher_id'] = callback.data

        await callback.message.delete()

        await UpdateTeacherState.choice_fild_callback.set()
        await callback.message.bot.send_message(chat_id=callback.message.chat.id , text = "Edit fild choice:" , reply_markup=teacher_fild_btn())

@dp.callback_query_handler(state=UpdateTeacherState.choice_fild_callback)
async def calback_teacher_fild_handler(callback: types.CallbackQuery, state= FSMContext):
    if callback.data == 'back':
        await callback.message.delete()
        teacher: List[UserDto] = User().select_all_teacher()
        await UpdateTeacherState.choice_teacher_callback.set()
        await callback.message.answer(text='Tanlang', reply_markup=teacher_inline_btn(teacher))

    else:
        async with state.proxy() as data:
            data['teacher_fild'] = callback.data
        if callback.data == 'name':
            await callback.message.delete()
            await UpdateTeacherState.new_value.set()
            await callback.message.bot.send_message(chat_id=callback.message.chat.id , text = 'Ism kiriting')
        else:
            await callback.message.delete()
            await UpdateTeacherState.new_value.set()
            await callback.message.bot.send_message(chat_id=callback.message.chat.id, text='Nomer kiriting☎️')

@dp.message_handler(state = UpdateTeacherState.new_value)
async def update_new_value_handler(message: types.Message , state = FSMContext):
    async with state.proxy() as data:
        data['new_value'] = message.text
    User().admin_update_teacher(data.get('new_value'), data.get('teacher_fild'),data.get('teacher_id'))
    await TeacherState.crud_choice.set()
    await message.answer(text= 'Mofaqiyatli o\'zgartirildi' , reply_markup=teacher_markup())