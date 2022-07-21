from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BACK_TEXT = '🔙Back'
BACK_INLINE_BTN = InlineKeyboardButton(text=BACK_TEXT, callback_data='back')


def back_inline_markup():
    markup = InlineKeyboardMarkup()
    markup.add(BACK_INLINE_BTN)

    return markup
