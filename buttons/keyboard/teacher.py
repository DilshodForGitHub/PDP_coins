from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# for all
BACK_TEXT = '🔙Back'
BACK_BTN = KeyboardButton(text=BACK_TEXT)

USER_TEXT = '👨‍💻 User'
USER_BTN = KeyboardButton(USER_TEXT)

TEACHER_TEXT = '🧑‍💼 Teacher'
TEACHER_BTN = KeyboardButton(TEACHER_TEXT)


# For Admin
ADD_TEACHER_TEXT = '➕ Add Teacher'
ADD_TEACHER_BTN = KeyboardButton(text = ADD_TEACHER_TEXT)

DELETE_TEACHER_TEXT = '❌ Delete Teacher'
DELETE_TEACHER_BTN = KeyboardButton(text = DELETE_TEACHER_TEXT)

UPDATE_TEACHER_TEXT = '🔄 Update Teacher'
UPDATE_TEACHER_BTN = KeyboardButton(text = UPDATE_TEACHER_TEXT)


# For Teacher
MY_INFO_TEXT = 'My info 📑'
MY_INFO_BTN = KeyboardButton(text=MY_INFO_TEXT)

MY_GROUP_TEXT = 'My groups 👥'
MY_GROUP_BTN = KeyboardButton(text=MY_GROUP_TEXT)

MY_STUDENTS_TEXT = 'My all group reyting 🏆'
MY_STUDENTS_BTN = KeyboardButton(text=MY_STUDENTS_TEXT)

# ASSESSMENT_OF_CHILDREN_TEXT = 'Assessment of children 🎖'
# ASSESSMENT_OF_CHILDREN_BTN = KeyboardButton(text=ASSESSMENT_OF_CHILDREN_TEXT)






def admin_teacher_markup():
    dizayin = [
        [ADD_TEACHER_BTN , DELETE_TEACHER_BTN],
        [UPDATE_TEACHER_BTN , BACK_BTN]
    ]
    markup = ReplyKeyboardMarkup(keyboard=dizayin, one_time_keyboard=True, resize_keyboard=True)
    return markup

def teacher_markup():
    dizayin = [
        [MY_INFO_BTN , MY_GROUP_BTN],
        [MY_STUDENTS_BTN , BACK_BTN]
    ]
    markup = ReplyKeyboardMarkup(keyboard=dizayin, one_time_keyboard=True, resize_keyboard=True)
    return markup







# Teacher btn

PHONE_TEXT = 'Phone ☎️'
PHONE_BTN = KeyboardButton(text=PHONE_TEXT , request_contact=True)


def teacher_phone_markup():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(PHONE_BTN)
    return markup

