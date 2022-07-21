import datetime
from typing import List

from db.dto import SubjectDTO
from db.transactions import Transactions


class Subject(Transactions):
    def __init__(self,
                 _id : int = None,
                 name: str = None,
                 delete_at: str = None,
                 create_by: int = None):
        super().__init__()
        self._id = _id
        self.name = name
        self.create_by = create_by
        self.delete_at = delete_at




    def insert_subject(self):
        sql_query_get_info = 'select s.* from subject s where name=%s AND is_active= %s'
        param = (self.name , True)
        subject = self.execute(sql_query_get_info , param, fetchone=True)
        if not subject:
            sql: str = "insert into subject(name , create_by) VALUES (%s, %s)"
            params = ( self.name , self.create_by)
            self.execute(sql, params, commit=True )
            return False
        else:
            return subject

    def select_all_subject(self):
        sql: str = "select * from subject where is_active = %s"
        all_subject = self.execute(sql,(True , ), fetchall=True)
        _: List[SubjectDTO] = []
        for i in all_subject:
            result = SubjectDTO(id=i[0] , name=i[1] , create_at = i[2] , delete_at=i[3] , create_by = i[4])
            _.append(result)
        return _

    def select_filter_id(self):
        sql: str = "select * from subject where id = %s AND is_active = %s"
        subject = self.execute(sql, (self._id,True), fetchone=True)
        subject_response =  SubjectDTO(id=subject[0], name=subject[1], create_at=subject[2], delete_at=subject[3], create_by=subject[4])

        return subject_response

    def delete_subject(self, _id):
        date_time = datetime.datetime.now()
        sql_subject: str = 'update subject set is_active = %s , create_at = %s where id = %s'
        sql_groups: str = 'update groups set is_active = %s , create_at = %s where subject_id = %s'
        param = (False ,date_time , _id)
        self.execute(sql_groups , param , commit=True)
        return self.execute(sql_subject, param, commit=True)

