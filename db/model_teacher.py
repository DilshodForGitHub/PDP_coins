import datetime
from typing import List

from db.dto import UserDto
from db.enum import ROLE
from db.transactions import Transactions


class User(Transactions):
    def __init__(self, id: int = None,
                 fullname: str = None,
                 role: str = None,
                 phone_number: str = None,
                 about: str = None,
                 photo: str = None,
                 delete_at: str = None,
                 chat_id: str = None,
                 created_by: int = None,
                 subject_id: int = None,
                 is_active: int = None):
        super().__init__()
        self.id = id
        self.fullname = fullname
        self.phone_number = phone_number
        self.about = about
        self.role = role or ROLE.CHILD.value
        self.photo = photo
        self.delete_at = delete_at
        self.chat_id = chat_id
        self.created_by = created_by
        self.subject_id = subject_id
        self.is_active = is_active

    def insert_user(self):
        sql_query_get_info = 'select u.* from users u where u.phone_number= %s AND u.role = %s'
        param = (self.phone_number, self.role)
        teacher = self.execute(sql_query_get_info, param, fetchone=True)
        if not teacher:
            sql: str = "insert into users(phone_number ,role,subject_id , created_by) VALUES (%s,%s,%s,%s)"
            params: tuple = (self.phone_number, self.role, self.subject_id, self.created_by)
            self.execute(sql, parameters=params, commit=True)
            return False
        else:
            return True

    def update_teacher(self):

        sql: str = "update users set name =%s , about=%s, photo=%s, chat_id=%s, subject_id=%s , is_active=%s where phone_number = %s AND role = %s"
        params: tuple = (self.fullname , self.about, self.photo , self.chat_id , self.subject_id ,True,self.phone_number , self.role)
        return self.execute(sql, parameters=params, commit=True)


    def select_all_teacher(self):
        sql: str = "select s.* from users s where is_active = %s"
        all_subject = self.execute(sql, (True,), fetchall=True)
        _: List[UserDto] = []
        for i in all_subject:
            result = UserDto(id=i[0], fullname=i[1], role=i[2], phone_number=i[3], about=i[4], photo=i[5],
                                create_at=i[6], delete_at=i[7], chat_id=i[8], created_by=i[9])
            _.append(result)
        return _

    def select_filter_teacher(self, _subject_id: int):
        sql: str = "select * from users where is_active = %s AND subject_id = %s"
        all_subject = self.execute(sql, (True, int(_subject_id)), fetchall=True)
        _: List[UserDto] = []
        for i in all_subject:
            result = UserDto(_id=i[0], fullname=i[1], role=i[2], phone_number=i[3], about=i[4], photo=i[5],
                                create_at=i[6], delete_at=i[7], chat_id=i[8], created_by=i[9])
            _.append(result)
        return _
    def select_chat_id(self):
        sql: str = "select * from users where chat_id = %s AND is_active = %s"
        params: tuple = (self.chat_id , True)
        user =  self.execute(sql , params , fetchone=True)
        user_response = UserDto(user[0] ,
                      user[1],
                      user[2],
                      user[3],
                      user[4],
                      user[5],
                      user[6],
                      user[7],
                      user[8],
                      user[9],
                      user[10],
                      user[11]
                      )
        return user_response


    def delete_teacher(self, _id):
        sql: str = 'delete from users s where s.id = %s'
        param = (_id,)
        return self.execute(sql, param, commit=True)

    def admin_update_teacher(self, _new_value, _teacher_fild, _id):
        if _teacher_fild == 'name':
            sql: str = 'update users set name=%s where id=%s'
            param = (_new_value, _id)
            return self.execute(sql, param, commit=True)
        elif _teacher_fild == 'phone_number':
            sql: str = 'update users u set phone_number=%s where id=%s'
            param = (_new_value, _id)
            return self.execute(sql, param, commit=True)

    def phone_number_check(self, login = False , register = False):
        if login:
            sql: str = 'select * from users where phone_number = %s AND is_active=%s'

            param = (self.phone_number,True)

            result = self.execute(sql, param, fetchone=True)
            return result
        elif register:
            sql: str = 'select * from users where phone_number = %s AND is_active=%s'
            param = (self.phone_number, False)
            result = self.execute(sql, param, fetchone=True)
            return result

