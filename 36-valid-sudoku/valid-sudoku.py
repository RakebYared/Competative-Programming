class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        row = {a:[0]*9 for a in range(9)}
        col = {a:[0]*9 for a in range(9)}
        square = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                board[i][j] = int(board[i][j])
                if row[i][board[i][j]-1]==0 and col[j][board[i][j]-1]==0 and board[i][j] not in square[(i//3, j//3)]:  
                    row[i][board[i][j]-1] = 1
                    col[j][board[i][j]-1] = 1
                    square[(i//3, j//3)].append(board[i][j])
                else:
                    return False
        return True