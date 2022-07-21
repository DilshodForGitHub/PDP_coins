from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from buttons.inline.auth import BACK_INLINE_BTN
from db.dto import GroupDto


def group_inline_btn(group: List[GroupDto]):
    markup = InlineKeyboardMarkup()
    for i in group:
        result = InlineKeyboardButton(text=f"Group:{i.name}({i.child_count})", callback_data=i._id)
        markup.add(result)
    markup.add(BACK_INLINE_BTN)
    return markup