class Task:
    def __init__(self, name: str, comments: str, status: str, due_date=None):
        self.name = name
        self.comments = comments
        self.status = status
        self.due_date = due_date
        self.checklist: dict[str, bool] = {}
        self.progress = 0

