from typing import List
from collections import defaultdict


class Solver:
    def __init__(self, board: List[List[int]]) -> None:
        """
        Initialize the solver by creating sets for rows, columns and 3x3 boxes. Add all the given numbers in the board
        to their corresponding sets and start solving the board. Does not return anything, board is solved inplace
        @param board: the given sudoku board
        @type board: List[List[int]]
        """
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    self.placeNumber(i, j, board[i][j], board)

        self.backtracking(board)

    def placeNumber(self, r: int, c: int, val: int, board: List[List[int]]) -> None:
        """
        Method to place the given value in the sudoku board at the given coordinates
        @param r: row at which the given value is to be placed
        @type r: int
        @param c: column at which the given value is to be placed
        @type c: int
        @param val: number to be placed at given row and column
        @type val: int
        @param board: current board in which the new value is to be placed
        @type board: List[List[int]]
        """
        board[r][c] = val
        self.rows[r].add(val)
        self.cols[c].add(val)
        self.boxes[(r // 3, c // 3)].add(val)

    def removeNumber(self, r: int, c: int, board: List[List[int]]) -> None:
        """
        Method to remove the value in the sudoku board at the given coordinates
        @param r: row at which the value is to be removed
        @type r: int
        @param c: column at which the value is to be removed
        @type c: int
        @param board: current board in which the value is to be removed
        @type board: List[List[int]]
        """
        val, board[r][c] = board[r][c], 0
        self.rows[r].remove(val)
        self.cols[c].remove(val)
        self.boxes[(r // 3, c // 3)].remove(val)

    def backtracking(self, board: List[List[int]]) -> bool:
        """
        Method to solve the given sudoku board using backtracking algorithm.
        @param board: given sudoku board
        @type board: List[List[int]]
        @return: True if sudoku is solved, False otherwise
        @rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    continue

                for val in range(1, 10):
                    if self.isValid(i, j, val):
                        self.placeNumber(i, j, val, board)

                        if self.backtracking(board):
                            return True
                        else:
                            self.removeNumber(i, j, board)

                # Could not place any number at current location
                return False

        # Completed solving the board
        return True

    def isValid(self, r: int, c: int, val: int) -> bool:
        """
        Method to determine if given value can be placed at given coordinates in O(1)
        @param r: row at which we need to check
        @type r: int
        @param c: column at which we need to check
        @type c: int
        @param val: value that is to be checked
        @type val: int
        @return: True if the value can be placed at given coordinates, False otherwise
        @rtype: bool
        """
        return not(val in self.rows[r] or val in self.cols[c] or val in self.boxes[(r // 3, c // 3)])
