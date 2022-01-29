def isValidSudoku(board):
    def checkSector(sector):
        valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(3):
            for j in range(3):
                if sector[i][j] in valid:
                    valid.remove(sector[i][j])
                elif sector[i][j] == '.':
                    pass
                else:
                    return False
        return True
    i = 0
    j = 0
    while True:
        currentSector = []
        for k in range(3):
            currentSector.append(board[k+i][j:j+3])
        if i == 0 or i == 3:
            i+=3
        elif i == 6:
            j+=3
            i=0
        if not checkSector(currentSector):
            return False
        if j >= 9:
            break

    def checkLines(board):
        for k in range(9):
            valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            sector = board[k][:]
            for l in range(9):
                if sector[l] in valid:
                    valid.remove(sector[l])
                elif sector[l] == '.':
                    pass
                else:
                    return False
        return True
    boardTranspose = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(9):
            boardTranspose[i].append(board[j][i])
    if not checkLines(board):
        return False
    if not checkLines(boardTranspose):
        return False
    return True
board = [['.', '.', '1', '1', '.', '.', '8', '.', '.'],
         ['.', '.', '2', '6', '.', '.', '9', '.', '.'],
         ['.', '.', '3', '7', '.', '.', '1', '.', '.'],
         ['.', '.', '4', '8', '.', '.', '2', '.', '.'],
         ['.', '.', '5', '9', '.', '.', '3', '.', '.'],
         ['.', '.', '6', '1', '.', '.', '4', '.', '.'],
         ['.', '.', '7', '2', '.', '.', '5', '.', '.'],
         ['.', '.', '8', '3', '.', '.', '6', '.', '.'],
         ['.', '.', '9', '4', '.', '.', '7', '.', '.']]
print(isValidSudoku(board))
