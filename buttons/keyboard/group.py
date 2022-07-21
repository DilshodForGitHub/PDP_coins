from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

BACK_TEXT = '🔙Back'
BACK_BTN = KeyboardButton(text=BACK_TEXT)

GROUP_TEXT = '👥Group'
GROUP_BTN = KeyboardButton(text=GROUP_TEXT)

ADD_GROUP_TEXT = '➕ Add Group'
ADD_GROUP_BTN = KeyboardButton(text=ADD_GROUP_TEXT)

DELETE_GROUP_TEXT = '❌ Delete Group'
DELETE_GROUP_BTN = KeyboardButton(text=DELETE_GROUP_TEXT)

UPDATE_GROUP_TEXT = '🔄 Update Group'
UPDATE_GROUP_BTN = KeyboardButton(text=UPDATE_GROUP_TEXT)

GROUP_TEACHER_TEXT = '👥 Group ➕ 🧑‍💼 Teacher'
GROUP_TEACHER_BTN = KeyboardButton(text=GROUP_TEACHER_TEXT)

GROUP_STUDENT_TEXT = '👥 Group ➕ 👩‍🎓👨‍🎓Student'
GROUP_STUDENT_BTN = KeyboardButton(text=GROUP_STUDENT_TEXT)


def group_markup():
    dizayin = [
        [ADD_GROUP_BTN, DELETE_GROUP_BTN],
        [UPDATE_GROUP_BTN, GROUP_TEACHER_BTN],
        [GROUP_STUDENT_BTN , BACK_BTN]
    ]
    markup = ReplyKeyboardMarkup(keyboard=dizayin, one_time_keyboard=True, resize_keyboard=True)
    return markup
