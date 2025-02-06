class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {r : set() for r in range(9)}
        cols = {c : set() for c in range(9)}
        square = {s : set() for s in range(9)}

        for row in rows:
            for c in range(9):
                if board[row][c]!='.' and board[row][c] in rows[row]:
                    return False
                else:
                    rows[row].add(board[row][c])
        
        for col in cols:
            for r in range(9):
                if board[r][col] != '.' and board[r][col] in cols[col]:
                    return False
                else:
                    cols[col].add(board[r][col])

        
        for r in range(9):
            for c in range(9):
                sq = (r//3)*3 + c//3
                if board[r][c] != '.' and board[r][c] in square[sq]:
                    return False   
                else:
                    square[sq].add(board[r][c])
        
        return True

        