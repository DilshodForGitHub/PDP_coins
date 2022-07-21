from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.inline.subject import subject_inline_btn
from buttons.keyboard.group import ADD_GROUP_TEXT, group_markup
from db.dto import SubjectDTO
from db.mapper import group_insert
from db.model_subject import Subject
from dispacher import dp
from states.admin.group import GroupState, AddGroupState


@dp.message_handler(lambda message: str(message.text).__eq__(ADD_GROUP_TEXT) , state=GroupState.crud_choice)
async def subject_handler(message: types.Message):
    subjects: List[SubjectDTO] = Subject().select_all_subject()

    await AddGroupState.choice_subject.set()
    await message.answer(text='Yaratadigan gurupani fanini belgilang : ' , reply_markup=subject_inline_btn(subjects))


@dp.callback_query_handler(state=AddGroupState.choice_subject)
async def callback_subject_handler(callback: types.CallbackQuery , state = FSMContext):
    if callback.data == 'back':
        await callback.message.delete()
        await GroupState.crud_choice.set()
        await callback.message.answer(text='Tanlang' , reply_markup=group_markup())

    else:
        async with state.proxy() as data:
            data['subject_id'] = callback.data
        await callback.message.delete()

        await AddGroupState.name.set()
        await callback.message.bot.send_message(chat_id=callback.message.chat.id , text= 'Gurupani nomini kiriting : ')

@dp.message_handler(state = AddGroupState.name)
async def group_name_handler(message: types.Message , state= FSMContext):
    async with state.proxy() as data:
        data['group_name'] = message.text
        data['chat_id'] = message.chat.id
    group = group_insert(data)
    response = group.insert_group()
    if not response:
        await message.delete()
        await GroupState.crud_choice.set()
        await message.answer(text="Gruppa Mofaqiyatli yaratildi ✅", reply_markup=group_markup())
    else:
        await GroupState.crud_choice.set()
        await message.answer(text='Bunday guruh mavjud ❌' , reply_markup=group_markup())


