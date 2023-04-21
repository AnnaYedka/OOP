from Entities.User import User
from Entities.Board import Board
from DBManagers.UserManager import UserManager
from DBManagers.BoardManager import BoardManager


class UserService:
    def __init__(self, user_manager: UserManager, board_manager: BoardManager):
        self.current_user: User = None
        self.user_manager = user_manager
        self.board_manager = board_manager

    def register(self, username: str, password: str):
        # add data validation
        self.current_user = User(username, password)

    def log_in(self, username: str, password: str) -> bool:
        user = self.user_manager.get_user_by_name(username)
        if user is None:
            raise LookupError("user not found")
        if user.password == password:
            self.current_user = user
            return True
        return False

    def log_out(self):
        self.current_user = None

    def delete_account(self):
        boards = self.board_manager.get_boards(self.current_user.board_ids)
        for board in boards:
            board.user_ids.remove(self.current_user.id)
            if len(board.user_ids) == 0:
                self.board_manager.remove_board(board.id)
        self.user_manager.remove_user(self.current_user.id)
        self.current_user = None

    def get_all_user_boards(self) -> list[Board]:
        return self.board_manager.get_boards(self.current_user.board_ids)

    def add_board(self, board: Board):
        self.current_user.board_ids.append(board)
        self.user_manager.update_users(self.current_user)


