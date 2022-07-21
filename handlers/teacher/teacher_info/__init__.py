from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.keyboard.teacher import MY_INFO_TEXT, teacher_markup
from db.dto import UserDto, SubjectDTO
from db.model_subject import Subject
from db.model_teacher import User
from dispacher import dp
from states.teacher import TeacherState


@dp.message_handler(lambda message: str(message.text).__eq__(MY_INFO_TEXT), state = TeacherState.teacher_menu_choice)
async def teacher_info_handler(message: types.Message , state = FSMContext):
    async with state.proxy() as data:
        data['chat_id'] = message.chat.id
    response: UserDto = User(chat_id=data.get('chat_id')).select_chat_id()
    subject: SubjectDTO = Subject(_id=response.subject_id).select_filter_id()
    text = f"""
I.F.SH : {response.fullname}
Telefon nomer : {response.phone_number}
Vazifasi : {response.role}
O'zim haqimda : {response.about}
Dars beradigan Fan : {subject.name}
    """
    await TeacherState.teacher_menu_choice.set()
    await message.bot.send_photo(chat_id=message.chat.id,photo=response.photo , caption = text , reply_markup=teacher_markup())