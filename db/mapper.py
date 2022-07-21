from db.model_group import Group
from db.model_subject import Subject


def subject_insert(data: dict):
    return Subject(
        name=data.get('name'),
        create_by=data.get('chat_id')
    )

def group_insert(data: dict):
    return Group(
        name=data.get('group_name'),
        subject_id=data.get('subject_id'),
        create_by=data.get('chat_id')
    )
