from typing import List
from collections import defaultdict


class Solver:
    def __init__(self, board: List[List[int]]) -> None:
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    self.placeNumber(i, j, board[i][j], board)

        self.backtracking(board)

    def placeNumber(self, r: int, c: int, val: int, board: List[List[int]]) -> None:
        board[r][c] = val
        self.rows[r].add(val)
        self.cols[c].add(val)
        self.boxes[(r // 3, c // 3)].add(val)

    def removeNumber(self, r: int, c: int, board: List[List[int]]) -> None:
        val, board[r][c] = board[r][c], 0
        self.rows[r].remove(val)
        self.cols[c].remove(val)
        self.boxes[(r // 3, c // 3)].remove(val)

    def backtracking(self, board: List[List[int]]) -> bool:
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

                return False

        return True

    def isValid(self, r: int, c: int, val: int) -> bool:
        return not(val in self.rows[r] or val in self.cols[c] or val in self.boxes[(r // 3, c // 3)])
