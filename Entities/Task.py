class Task:
    def __init__(self, name: str, comments: str, status: str, due_date=None):
        self.id: int = None
        self.name = name
        self.comments = comments
        self.status = status
        self.due_date = due_date


class TaskWithChecklist(Task):
    def __init__(self, name: str, comments: str, status: str, due_date=None):
        Task.__init__(name, comments, status, due_date)
        self.checklist: list[Subtask] = []
        self.progress = 0


class Subtask:
    def __init__(self, name: str):
        self.name = name
        self.done = False
