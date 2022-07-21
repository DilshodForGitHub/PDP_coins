
class BaseDto:
    def __init__(self , create_at: str = None,
                 delete_at : str = None):
        self.create_at = create_at
        self.delete_at = delete_at

class SubjectDTO(BaseDto):
    def __init__(self, id: int = None,
                 name: str = None,
                 create_at: str = None,
                 delete_at: str = None,
                 create_by: int = None):
        super().__init__(create_at, delete_at)
        self.id = id
        self.name = name
        self.create_by = create_by



class UserDto(BaseDto):
    def __init__(self, _id: int = None,
                 fullname : str = None,
                 role : str = None,
                 phone_number: str = None,
                 about: str = None ,
                 photo: str = None,
                 create_at: str = None,
                 delete_at: str = None,
                 chat_id: int = None,
                 created_by: str = None,
                 subject_id: int = None,
                 is_active :bool = None
                 ) -> None :
        super().__init__(create_at , delete_at)
        self._id = _id
        self.fullname = fullname
        self.role = role
        self.phone_number = phone_number
        self.about = about
        self.photo = photo
        self.chat_id = chat_id
        self.created_by = created_by
        self.subject_id = subject_id
        self.is_active = is_active


class GroupDto(BaseDto):
    def __init__(self,
                 _id : int = None,
                 name: str = None,
                 subject_id: str = None,
                 teacher_id: str = None,
                 child_count: str = None,
                 create_at : str = None,
                 delete_at : str = None,
                 create_by : int = None,
                 start_time : int = None,
                 end_time : int = None,
                 day_bool : bool = None,
                 continue_month : int = None,
                 is_active : int = None,
                 delete_by : int = None
                 ) ->None:
        super().__init__(create_at , delete_at)
        self._id = _id
        self.name = name
        self.subject_id = subject_id
        self.teacher_id = teacher_id
        self.child_count = child_count
        self.create_by = create_by
        self.start_time = start_time
        self.end_time = end_time
        self.day_bool = day_bool
        self.continue_month = continue_month
        self.is_active = is_active
        self.delete_by = delete_by


class ChildrenDto(BaseDto):
    def __init__(self, first_name: str = None,
                 last_name: str = None,
                 phone: str = None ,
                 group_id: int = None) -> None:
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.group_id = group_id



