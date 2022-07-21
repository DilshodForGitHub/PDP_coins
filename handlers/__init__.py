from buttons.keyboard.auth import role_markup
from db.dto import UserDto


from handlers.admin.admin_handler import *

from handlers.admin.create.subject import *
from handlers.admin.create.teacher import *
from handlers.admin.create.group import *

from handlers.admin.delete.subject import *
from handlers.admin.delete.teacher import *
from handlers.admin.delete.group import *

from handlers.admin.update.teacher import *
from handlers.admin.update.group_teacher_add import *
from handlers.admin.update.group_student_add import *

from handlers.teacher.teacher_handler import *
from handlers.teacher.teacher_info import *
from handlers.teacher.my_group import *






from aiogram import types

from dispacher import dp


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):


    await message.answer_photo(photo=open('media/img.png', mode='rb'), caption='Welcome')
    await message.answer(text='Quydagi role lardan birini tanlang', reply_markup=role_markup())
