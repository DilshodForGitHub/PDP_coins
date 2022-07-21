from typing import List

from aiogram import types

from buttons.inline.subject import subject_inline_btn
from buttons.keyboard.group import GROUP_STUDENT_TEXT
from db.dto import SubjectDTO
from db.model_subject import Subject
from dispacher import dp
from states.admin.group import GroupState
from states.admin.group_student_add import GroupStudentState


@dp.message_handler(lambda message: str(message.text).__eq__(GROUP_STUDENT_TEXT), state =GroupState.crud_choice)
async def group_student_text_handler(message: types.Message):
    await GroupStudentState.subject.set()
    subject : List[SubjectDTO] = Subject().select_all_subject()

    await message.answer(text = 'Gurupani yonalishini tanlang !' , reply_markup=subject_inline_btn(subject))