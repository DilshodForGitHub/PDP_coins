from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from buttons.inline.auth import BACK_INLINE_BTN
from db.dto import SubjectDTO


def subject_inline_btn(subject: List[SubjectDTO]):
    markup = InlineKeyboardMarkup()
    for i in subject:
        result = InlineKeyboardButton(text=i.name, callback_data=i.id)
        markup.add(result)
    markup.add(BACK_INLINE_BTN)
    return markup