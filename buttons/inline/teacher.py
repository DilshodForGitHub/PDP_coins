from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from buttons.inline.auth import BACK_INLINE_BTN
from db.dto import UserDto


def teacher_inline_btn(teachers: List[UserDto]):
    markup = InlineKeyboardMarkup()
    for i in teachers:
        result = InlineKeyboardButton(text=f"""Name : {i.fullname} Tel : {i.phone_number}""", callback_data=i._id)
        markup.add(result)
    markup.add(BACK_INLINE_BTN)
    return markup


def teacher_fild_btn():
    markup = InlineKeyboardMarkup(row_width=2)
    teacher_update_filds ={'fullname':'name' ,'phone':'phone_number'}
    for key , value in teacher_update_filds.items():
        markup.add(InlineKeyboardButton(text=key ,callback_data=value))


    markup.add(BACK_INLINE_BTN)

    return markup

