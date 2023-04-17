

class Board:
    def __init__(self, name: str):
        self.id: int = None
        self.name = name
        self.tasks = []  #: list[Task]
        self.user_ids: list[int] = []
        self.task_statuses: list[str] = []