from typing import List

from aiogram import types

from buttons.inline.subject import subject_inline_btn
from buttons.keyboard.subject import DELETE_SUBJECT_TEXT, subject_markup
from db.dto import SubjectDTO
from db.model_subject import Subject
from dispacher import dp
from states.admin.subject import DeleteSubjectState, SubjectState


@dp.message_handler(lambda message: str(message.text).__eq__(DELETE_SUBJECT_TEXT) , state=SubjectState.crud_choice)
async def delete_subject_handler(message: types.Message):
    subjects: List[SubjectDTO] = Subject().select_all_subject()
    await DeleteSubjectState.delete_callback.set()

    await message.answer(text='Fan nomi kiriting' , reply_markup=subject_inline_btn(subjects))


@dp.message_handler(state=DeleteSubjectState.delete_callback)
async def delete_text_handler(message: types.Message):
    await message.delete()

@dp.callback_query_handler(state=DeleteSubjectState.delete_callback)
async def callback_query_for_subject(callback: types.CallbackQuery):
    if callback.data =='back':
        await callback.message.delete()
        await SubjectState.crud_choice.set()
        await callback.message.answer(text='Tanlang', reply_markup=subject_markup())
    else:
        Subject().delete_subject(int(callback.data))
        await callback.message.delete()

        subjects: List[SubjectDTO] = Subject().select_all_subject()
        await DeleteSubjectState.delete_callback.set()
        await callback.message.answer(text='Fan nomi kiriting' , reply_markup=subject_inline_btn(subjects))




