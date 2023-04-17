from Entities.Board import Board
from UserManager import UserManager

class BoardManager:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = BoardManager()
        return cls.__instance

    def __init__(self):
        if BoardManager.__instance is None:
            self.boards: list[Board] = []

    def add_board(self, board: Board):
        self.boards.append(board)

    def get_board(self, board_id: int) -> Board:
        for board in self.boards:
            if board.id == board_id:
                return board
        return None

    def update_board(self, changed_board: Board):
        found = False
        for board in self.boards:
            if board.id == changed_board.id:
                board = changed_board
                found = True
        if not found:
            raise LookupError("board not found")

    def remove_board(self, board_id: int):
        found = False
        for board in self.boards:
            if board.id == board_id:
                found = True
                self.boards.remove(board)
                UserManager.get_instance().remove_board_from_users(board_id, board.user_ids)
        if not found:
            raise LookupError("board not found")

    def add_users_to_board(self, board_id: int, *user_ids: int):
        board = self.get_board(board_id)
        for user_id in user_ids:
            board.user_ids.append(user_id)

        UserManager.get_instance().add_board_to_users(board_id, user_ids)

    def remove_users_from_board(self, board_id: int, *user_ids: int):
        board = self.get_board(board_id)
        for user_id in user_ids:
            board.user_ids.remove(user_id)

        UserManager.get_instance().remove_board_from_users(board_id, user_ids)

