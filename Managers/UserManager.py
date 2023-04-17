from Entities.User import User


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
                found_user = True
                self.users.remove(user)
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
