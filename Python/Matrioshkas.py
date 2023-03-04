
def isValidSudoku(board):
    row = {}
    column = {}
    box = {}
    for i,n in enumerate(board):
        row[i] = {}
        for k in n:
            if k != '.':
                if k not in row[i]: 
                    row[i][k] = 1
                else:
                    print('hello1')
                    return False
    for i in range(len(board)):
        column[i] = {}
        for j in board:
            if j[i] != ".":
                if j[i] not in column[i]: 
                    column[i][j[i]] = 1
                else:
                    print('hello2')
                    return False
    for i in range(0,len(board),3):
        for j in range(0,len(board),3):
            box[tuple([i,j])] = {}
            for x in range(i,i+3):
                for y in range(j,j+3):
                    if board[x][y] != '.':
                        if board[x][y] not in box[i,j]:
                            box[i,j][board[x][y]] = 1
                        else:
                            print("hello3")
                            return False    
    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))