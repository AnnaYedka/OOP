from Entities.Board import Board
from Entities.Task import *
from DBManagers.BoardManager import BoardManager
from DBManagers.UserManager import UserManager


class BoardService:
    def __init__(self, board_manager: BoardManager, user_manager: UserManager):
        self.board_manager = board_manager
        self.user_manager = user_manager
        self.current_board: Board = None

    def create_board(self, board_name: str, user):
        board = Board(board_name)
        self.board_manager.add_board(board)
        self.current_board = board
        self.add_users_to_board(user.id)

    def select_board(self, board: Board):
        self.current_board = board

    def remove_users_from_board(self, *user_ids: int):
        users = self.user_manager.get_users(*user_ids)
        for user in users:
            user.board_ids.remove(self.current_board.id)
        self.user_manager.update_users(*users)

    def add_users_to_board(self, *user_ids: int):
        self.current_board.user_ids.append(*user_ids)
        self.board_manager.update_boards(self.current_board)
        users = self.user_manager.get_users(*user_ids)
        for user in users:
            user.board_ids.append(self.current_board.id)
        self.user_manager.update_users(*users)

    def rename_board(self, new_name: str):
        self.current_board.name = new_name
        self.board_manager.update_boards(self.current_board)

    # task methods

    def add_status_list(self, status_name: str):
        self.current_board.task_statuses.append(status_name)
        self.board_manager.update_boards(self.current_board)

    def add_task(self, status: str, task_name: str, task_comments: str, due_date = None):
        task = Task(task_name, task_comments, status, due_date)
        self.current_board.tasks.append(task)
        self.board_manager.update_boards(self.current_board)

    def add_subtask(self, selected_task: Task, subtask_name: str):
        selected_task.checklist.update({subtask_name: False})
        self.board_manager.update_boards(self.current_board)

    def move_task(self, selected_task: Task, status_moved_to: str):
        selected_task.status = status_moved_to
        self.board_manager.update_boards(self.current_board)

    def mark_subtask(self, selected_task: Task, subtask: str):
        selected_task.checklist[subtask] = True
        selected_task.progress += 1
        self.board_manager.update_boards(self.current_board)

    def rename_task(self, selected_task: Task, new_name: str):
        selected_task.name = new_name
        self.board_manager.update_boards(self.current_board)

    def change_task_comments(self, selected_task: Task, new_comments: str):
        selected_task.comments = new_comments
        self.board_manager.update_boards(self.current_board)

    def change_task_due_date(self, selected_task: Task, new_date):
        selected_task.due_date = new_date
        self.board_manager.update_boards(self.current_board)

    def remove_task(self, selected_task: Task):
        self.current_board.tasks.remove(selected_task)
        self.board_manager.update_boards(self.current_board)

    def show_tasks(self):
        for task in self.current_board.tasks:
            print("------------")
            print(task.name)
            print(task.comments)
            print(task.status)
            print(task.checklist)
            print(task.progress, "/", len(task.checklist))

