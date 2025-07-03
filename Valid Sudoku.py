import collections
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
cols = collections.defaultdict(set)
rows = collections.defaultdict(set)
squeares = collections.defaultdict(set)

for r in range(9):
    for c in range(9):
        if board[r][c] == '.':
            continue
        if (board[r][c] in rows[r] or
            board[r][c] in cols[c] or
            board[r][c] in squeares[(r//3, c//3)]):
            print("False")
        cols[c].add(board[r][c])
        rows[r].add(board[r][c])
        squeares[(r//3, c//3)].add(board[r][c])
print('True')