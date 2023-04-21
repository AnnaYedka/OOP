from Entities.Board import Board
from UserManager import UserManager


class BoardManager:
    def __init__(self):
        self.boards: list[Board] = []

    def add_board(self, board: Board):
        self.boards.append(board)

    def get_boards(self, *board_ids: int) -> list[Board]:
        return [board for board in self.boards if board.id in board_ids]

    def update_boards(self, *changed_boards: Board):
        for upd_board in changed_boards:
            for i in range(len(self.boards)):
                if upd_board.id == self.boards[i].id:
                    self.boards[i] = upd_board

    def remove_board(self, board_id: int):
        found = False
        for board in self.boards:
            if board.id == board_id:
                found = True
                self.boards.remove(board)
        if not found:
            raise LookupError("board not found")
