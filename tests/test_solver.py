from sudoku.solver import Solver


def test_solver():
    board, result = [], []

    with open('test_sudoku.txt', 'r') as fp:
        for _ in range(9):
            row = fp.readline().strip().split(' ')
            board.append([int(x) for x in row])

        fp.readline()

        for _ in range(9):
            row = fp.readline().strip().split(' ')
            result.append([int(x) for x in row])

    sk = Solver(board)
    for i in range(9):
        for j in range(9):
            assert result[i][j] == board[i][j]

    print(f'Test passed')


test_solver()
