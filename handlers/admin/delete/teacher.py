from typing import List

from aiogram import types

from buttons.inline.teacher import teacher_inline_btn
from buttons.keyboard.teacher import DELETE_TEACHER_TEXT, teacher_markup
from db.dto import UserDto

from db.model_teacher import User
from dispacher import dp
from states.admin.teacher import DeleteTeacherState, TeacherState


@dp.message_handler(lambda message: str(message.text).__eq__(DELETE_TEACHER_TEXT) , state=TeacherState.crud_choice)
async def delete_teacher_handler(message: types.Message):
    teacher: List[UserDto] = User().select_all_teacher()
    await DeleteTeacherState.delete_callback.set()
    await message.bot.send_message(chat_id=message.chat.id , text = 'O\'qtuvchilar ro\'yhati' , reply_markup=teacher_inline_btn(teacher))



@dp.message_handler(state=DeleteTeacherState.delete_callback)
async def delete_text_handler(message: types.Message):
    await message.delete()




@dp.callback_query_handler(state=DeleteTeacherState.delete_callback)
async def callback_delete_teacher_handler(callback: types.CallbackQuery):
    if callback.data == 'back':
        await callback.message.delete()
        await TeacherState.crud_choice.set()
        await callback.message.answer(text='Tanlang', reply_markup=teacher_markup())
    else:
        User().delete_teacher(int(callback.data))
        await callback.message.delete()

        teacher: List[UserDto] = User().select_all_teacher()
        await DeleteTeacherState.delete_callback.set()
        await callback.message.answer(text='Fan nomi kiriting', reply_markup=teacher_inline_btn(teacher))


