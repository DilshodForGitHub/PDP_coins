from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from buttons.keyboard.group import GROUP_BTN
from buttons.keyboard.subject import SUBJECT_BTN, ADD_SUBJECT_BTN, DELETE_SUBJECT_BTN, UPDATE_SUBJECT_BTN
from buttons.keyboard.teacher import USER_BTN, TEACHER_BTN

BACK_TEXT = '🔙Back'
BACK_BTN = KeyboardButton(text=BACK_TEXT)


def role_markup():
    dizayin = [
        [USER_BTN, TEACHER_BTN]
    ]
    markup = ReplyKeyboardMarkup(keyboard=dizayin, one_time_keyboard=True, resize_keyboard=True)
    return markup


def admin_markup():
    dizayn = [
        [SUBJECT_BTN, TEACHER_BTN],
        [GROUP_BTN,BACK_BTN]
    ]
    markup = ReplyKeyboardMarkup(keyboard=dizayn, one_time_keyboard=True, resize_keyboard=True)
    return markup




