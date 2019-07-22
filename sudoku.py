from os import system


board = [[4, 0, 6, 0, 8, 0, 0, 0, 0],
		 [0, 0, 9, 2, 0, 4, 0, 6, 0],
		 [5, 0, 1, 0, 0, 0, 0, 0, 0],
		 [3, 1, 7, 0, 0, 2, 0, 0, 0],
		 [0, 0, 0, 6, 0, 5, 0, 0, 0],
		 [0, 0, 0, 1, 0, 0, 9, 8, 3],
		 [0, 0, 0, 0, 0, 0, 2, 0, 1],
		 [0, 5, 0, 7, 0, 3, 6, 0, 0],
		 [0, 0, 0, 0, 6, 0, 3, 0, 4]]


solved = False
by_step = False 


def get_row(board):
	for line in board:
		yield line


def get_column(board):
	for i in range(9):
		yield [board[j][i] for j in range(9)]


def get_block(board):
	pos = [0, 3, 6]
	for x in pos:
		for y in pos:
			block = []
			for i in range(0, 3):
				for j in range(0, 3):
					block.append(board[x + i][y + j])
			yield block


def contain_duplicate(arr):
	for i in range(len(arr) - 1):
		for j in range(i + 1, len(arr)):
			if arr[i] != 0 and arr[j] != 0 and arr[i] == arr[j]:
				return True
	return False


def is_valid(board):
	for row in get_row(board):
		if contain_duplicate(row):
			return False
	for column in get_column(board):
		if contain_duplicate(column):
			return False
	for block in get_block(board):
		if contain_duplicate(block):
			return False
	return True


def print_board(board):
	for line in board:
		print(" ".join(map(str, line)))
	print()


def solve(i, j):
	if i == 9:
		return 1
	if j == 9:
		return solve(i + 1, 0)
	if board[i][j] != 0:
		return solve(i, j + 1)
	else:
		for number in range(1,10):
			board[i][j] = number
			if is_valid(board):
				if solve(i, j + 1) == 1:
					return 1
		board[i][j] = 0


solve(0, 0)
# print_board(board)