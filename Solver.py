from typing import Tuple, List, Optional


class Solver:
    """
    Solver class to solve the given sudoku board in place
    """

    def __init__(self, board: List[List[int]]) -> None:
        """
        Initialized the solver class and set the instance parameters
        :param board: Copy of the sudoku board that needs to be solved
        :type board: list[list[int]]
        :returns: NA
        :rtype: NA
        """
        self.board = board
        self.backtracking()

    def backtracking(self) -> bool:
        """
        Solves the given sudoku board inplace using backtracking
        :return: Returns true or false based on whether the given sudoku board can be solved or not
        :rtype: bool
        """
        cell = self.getEmptyCell()

        if cell:
            row, col = cell
        else:
            return True

        for i in range(1, 10):
            if self.isValidPlacement(row, col, i):
                self.board[row][col] = i

                if self.backtracking():
                    return True

                self.board[row][col] = 0

        return False

    def getEmptyCell(self) -> Optional[Tuple[int, int]]:
        """
        Method to return row and column index of the first empty cell
        :return: row, column of the first empty cell. None if there is no empty cell
        :rtype: tuple(int, int)
        """
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j

        return None

    def isValidPlacement(self, row: int, col: int, value: int) -> bool:
        """
        Method to check if the given number can be placed in the given row and column in the given board
        :param row: Row of the board
        :type row: int
        :param col: Column of the board
        :type col: int
        :param value: Number to be placed in board[row][col]
        :type value: int
        :return: Returns true or false after checking the row, column and the 3x3 box for duplicate of given number
        :rtype: bool
        """

        # Check for duplicate in the column
        for r in range(9):
            if self.board[r][col] == value:
                return False

        # Check for duplicate in the row
        for c in range(9):
            if self.board[row][c] == value:
                return False

        box_row = row // 3
        box_col = col // 3

        # Check for duplicate in the 3x3 box
        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_row * 3 + 3):
                if self.board[i][j] == value:
                    return False

        return True
