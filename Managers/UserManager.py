from Entities.User import User
from BoardManager import BoardManager

class UserManager:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = UserManager()
        return cls.__instance

    def __init__(self):
        if UserManager.__instance is None:
            self.users: list[User] = []
            self.current_user_id: int = None

    def add_user(self, user: User):
        self.users.append(user)

    def remove_user(self, user_id: int):
        found_user = False
        for user in self.users:
            if user.id == user_id:
                for board_id in user.board_ids:
                    self.users.remove(user)
                    BoardManager.get_instance().remove_users_from_board(board_id, user_id)
                found_user = True
        if not found_user:
            raise LookupError("user not found")

    def log_in(self, username: str, password: str):
        for user in self.users:
            if user.name == username and user.password == password:
                self.current_user_id = user.id
        if self.current_user_id is None:
            raise LookupError("user not found")

    def log_out(self):
        self.current_user_id = None

    def get_users_by_id(self, *user_ids: int) -> list[User]:
        return [user for user in self.users if user.id in user_ids]

    def add_board_to_users(self, board_id: int, *user_ids: int):
        for user in self.users:
            if user.id in user_ids:
                user.board_ids.append(board_id)

    def remove_board_from_users(self, board_id: int, *user_ids: int):
        for user in self.users:
            if user.id in user_ids:
                user.board_ids.remove(board_id)
