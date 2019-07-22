import sudoku as solving

with open("sudoku.txt","r") as f:
    data = f.readlines()
    result, index = 0, 0
    for i in range(50):
        index += 1
        currentBoard = []
        for j in range(9):
            line = list(map(int, data[index].strip()))
            currentBoard.append(list(line))
            index += 1
        solving.board = list(currentBoard)
        print("Solving board", i)
        solving.solve(0, 0)
        result += solving.board[0][0] * 100 + solving.board[0][1] * 10 + solving.board[0][2]

print(result)
