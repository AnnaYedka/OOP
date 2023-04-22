from Entities.User import User

class UserManager:

    def __init__(self):
        self.users: list[User] = []

    def add_user(self, user: User):
        self.users.append(user)

    def remove_user(self, user_id: int):
        found_user = False
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                found_user = True
        if not found_user:
            raise LookupError("user not found")

    def get_users(self, *user_ids: int) -> list[User]:
        return [user for user in self.users if user.id in user_ids]

    def update_users(self, *updated_users: User):
        for upd_user in updated_users:
            for i in range(len(self.users)):
                if upd_user.id == self.users[i].id:
                    self.users[i] = upd_user

    def get_user_by_name(self, username: str) -> User:
        for user in self.users:
            if user.name == username:
                return user
        return None

