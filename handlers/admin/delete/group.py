from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.inline.group import group_inline_btn
from buttons.inline.subject import subject_inline_btn
from buttons.keyboard.group import DELETE_GROUP_TEXT, group_markup
from db.dto import SubjectDTO, GroupDto
from db.model_group import Group
from db.model_subject import Subject
from dispacher import dp
from states.admin.group import DeleteGroupState, GroupState


@dp.message_handler(lambda message: str(message.text).__eq__(DELETE_GROUP_TEXT) , state=GroupState.crud_choice)
async def delete_subject_handler(message: types.Message):
    subjects: List[SubjectDTO] = Subject().select_all_subject()
    await DeleteGroupState.choice_subject.set()

    await message.answer(text="O'chirmoqchi bo'lgan guruhni yo'nalishini tanlang 👇" , reply_markup=subject_inline_btn(subjects))

@dp.callback_query_handler(state=DeleteGroupState.choice_subject)
async def callback_subject_handler(callback: types.CallbackQuery , state = FSMContext):
    if callback.data == 'back':
        await callback.message.delete()
        await GroupState.crud_choice.set()
        await callback.message.answer(text='Tanlang' , reply_markup=group_markup())

    else:
        async with state.proxy() as data:
            data['subject_id'] = callback.data
            

        group: List[GroupDto]= Group().select_all_group(data.get('subject_id'))
        await callback.message.delete()
        await DeleteGroupState.delete_callback.set()
        await callback.message.bot.send_message(chat_id=callback.message.chat.id , text= "Tanlang",reply_markup=group_inline_btn(group))

    @dp.callback_query_handler(state=DeleteGroupState.delete_callback)
    async def callback_delete_group_handler(callback: types.CallbackQuery, state = FSMContext):
        if callback.data == 'back':
            await callback.message.delete()
            subjects: List[SubjectDTO] = Subject().select_all_subject()
            await DeleteGroupState.choice_subject.set()
            await callback.message.answer(text="O'chirmoqchi bo'lgan guruhni yo'nalishini tanlang 👇",
                                 reply_markup=subject_inline_btn(subjects))
        else:
            async with state.proxy() as data:
                data['group_id'] = callback.data
                data['chat_id'] = callback.message.chat.id
            await callback.message.delete()
            Group().is_active_false(data.get('group_id'),data.get('chat_id'))
            subjects: List[SubjectDTO] = Subject().select_all_subject()
            await DeleteGroupState.choice_subject.set()
            await callback.message.bot.send_message(chat_id=callback.message.chat.id , text = "Yana o'chirmoqchi bo'ganizni belgilang" , reply_markup=subject_inline_btn(subjects))





