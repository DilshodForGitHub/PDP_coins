from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

BACK_TEXT = '🔙Back'
BACK_BTN = KeyboardButton(text=BACK_TEXT)

SUBJECT_TEXT = '📚 Subject'
SUBJECT_BTN = KeyboardButton(text = SUBJECT_TEXT)

ADD_SUBJECT_TEXT = '➕ Add Subject'
ADD_SUBJECT_BTN = KeyboardButton(text = ADD_SUBJECT_TEXT)

DELETE_SUBJECT_TEXT = '❌ Delete Subject'
DELETE_SUBJECT_BTN = KeyboardButton(text = DELETE_SUBJECT_TEXT)

UPDATE_SUBJECT_TEXT = '🔄 Update Subject'
UPDATE_SUBJECT_BTN = KeyboardButton(text = UPDATE_SUBJECT_TEXT)




def subject_markup():
    dizayin = [
        [ADD_SUBJECT_BTN , DELETE_SUBJECT_BTN],
        [UPDATE_SUBJECT_BTN , BACK_BTN]
    ]
    markup = ReplyKeyboardMarkup(keyboard=dizayin, one_time_keyboard=True, resize_keyboard=True)
    return markup