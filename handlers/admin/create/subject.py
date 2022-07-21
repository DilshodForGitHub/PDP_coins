from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.inline.auth import back_inline_markup
from buttons.keyboard.subject import ADD_SUBJECT_TEXT, subject_markup
from db.mapper import subject_insert
from dispacher import dp
from states.admin.subject import AddSubjectState, SubjectState


@dp.message_handler(lambda message: str(message.text).__eq__(ADD_SUBJECT_TEXT) , state=SubjectState.crud_choice)
async def subject_handler(message: types.Message):
    await AddSubjectState.name.set()
    await message.answer(text='Fan nomi kiriting' , reply_markup=back_inline_markup())

@dp.callback_query_handler(state = AddSubjectState.name)
async def callback_back_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await SubjectState.crud_choice.set()
    await callback.message.bot.send_message(chat_id=callback.message.chat.id , text = 'Choice' ,reply_markup=subject_markup() )


@dp.message_handler(state= AddSubjectState.name)
async def add_subjecthandler(message: types.Message, state = FSMContext):
    async with state.proxy()  as data:
        data['name'] = message.text
        data['chat_id'] = message.chat.id
    subject = subject_insert(data)
    response = subject.insert_subject()
    if not response:
        await SubjectState.crud_choice.set()
        await message.bot.send_message(chat_id=message.chat.id,text='Successful' , reply_markup=subject_markup())
    else:
        await SubjectState.crud_choice.set()
        await message.bot.send_message(chat_id=message.chat.id, text='Bunday nomli subject yaratilgan !❌', reply_markup=subject_markup())