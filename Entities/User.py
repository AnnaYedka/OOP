class User:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password
        self.board_ids = []
        self.id: int
