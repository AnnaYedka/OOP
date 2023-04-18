from BoardManager import BoardManager
from Entities.Task import Task


class TaskManager:

    def add_task(self, board_id: int, task: Task):
        board_manager = BoardManager.get_instance()
        updated_board = board_manager.get_board(board_id)
        updated_board.tasks.append(task)
        board_manager.update_board(updated_board)

    def remove_task(self, board_id: int, task_id: int):
        board_manager = BoardManager.get_instance()
        updated_board = board_manager.get_board(board_id)
        for task in updated_board.tasks:
            if task.id == task_id:
                updated_board.tasks.remove(task)
        board_manager.update_board(updated_board)

    def update_task(self, board_id: int, task: Task):
        board_manager = BoardManager.get_instance()
        updated_board = board_manager.get_board(board_id)
        board_tasks = updated_board.tasks
        for i in range(len(board_tasks)):
            if board_tasks[i].id == task.id:
                board_tasks[i] = task
        board_manager.update_board(updated_board)

