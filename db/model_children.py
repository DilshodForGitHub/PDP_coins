from db.transactions import Transactions


class Child(Transactions):
    def __init__(self, first_name: str = None,
                 last_name: str = None,
                 phone: str = None ,
                 lesson_active_coins: int = 0,
                 home_work_coins: int = 0,
                 control_work_coins : int = 0,
                 coins: int = 0,
                 subject_id : int =None ,
                 group_id: int = None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.lesson_active_coins = lesson_active_coins
        self.home_work_coins = home_work_coins
        self.control_work_coins = control_work_coins
        self.coins = coins
        self.subject_id = subject_id
        self.group_id = group_id


