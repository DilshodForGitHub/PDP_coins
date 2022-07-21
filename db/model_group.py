import datetime
from typing import List

from db.dto import GroupDto
from db.transactions import Transactions


class Group(Transactions):
    def __init__(self, _id : int = None,
                 name: str = None,
                 subject_id: int = None,
                 teacher_id: int = None,
                 child_count: int = None,
                 delete_at: str = None,
                 create_by: int = None,
                 start_time: int = None,
                 end_time: int = None,
                 day_bool: bool = None,
                 continue_month: int = None,
                 is_active: int = None):
        super().__init__()
        self._id = _id
        self.name = name
        self.subject_id = subject_id
        self.teacher_id = teacher_id
        self.child_count = child_count or 0
        self.delete_at = delete_at
        self.create_by = create_by
        self.start_time = start_time
        self.end_time = end_time
        self.day_bool = day_bool
        self.continue_month = continue_month
        self.is_active = is_active or True

    def insert_group(self):
        sql_query_get_info = 'select * from groups where name=%s AND subject_id =%s'
        param = (self.name, self.subject_id)
        group = self.execute(sql_query_get_info, param, fetchone=True)
        if not group:
            sql: str = "insert into groups(name , subject_id,teacher_id , child_count ,delete_at, create_by , start_time , end_time , day_bool , continue_month, is_active) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s, %s)"
            params = (self.name, self.subject_id, self.teacher_id, self.child_count,self.delete_at, self.create_by, self.start_time,
                      self.end_time, self.day_bool, self.continue_month, self.is_active)
            self.execute(sql, params, commit=True)
            return False
        else:
            return group

    def select_all_group(self, _subject_id):
        sql: str = "select * from groups where subject_id = %s AND is_active= %s"
        param = (_subject_id , True)
        all_group = self.execute(sql,param, fetchall=True)
        _: List[GroupDto] = []
        for i in all_group:
            result = GroupDto(_id=i[0] ,
                              name=i[1] ,
                              subject_id = i[2] ,
                              teacher_id=i[3] ,
                              child_count = i[4],
                              create_at=i[5] ,
                              delete_at=i[6] ,
                              create_by=i[7],
                              start_time=i[8],
                              end_time=i[9],
                              day_bool=i[10],
                              continue_month=i[11],
                              is_active=i[12]
                              )
            _.append(result)
        return _
    def is_active_false(self, _id , _delete_by_id):
        delete_at = str(datetime.datetime.now())
        sql: str = 'update groups set is_active=%s , delete_by = %s , delete_at=%s where id=%s'
        params = (False,_delete_by_id, delete_at, _id)
        return self.execute(sql, params, commit=True)

    def update_group(self):
        sql: str = 'update groups set teacher_id=%s where id=%s AND is_active = %s'
        param = (self.teacher_id , self._id , True)
        return self.execute(sql, param, commit=True)

    def filter_group_teacher_id(self):
        sql: str = 'select * from groups where teacher_id=%s AND is_active= %s'
        params = (self.teacher_id , True)

        groups =  self.execute(sql, params , fetchall=True)
        _: List[GroupDto] = []

        for i in groups:
            __ = GroupDto(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13])
            _.append(__)

        return _





