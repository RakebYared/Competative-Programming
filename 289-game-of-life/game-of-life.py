class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        def inbound(r,c):
            if r < 0 or r == row or c < 0 or c == col:
                return False
            else:
                return True

        direction = [(1, 1), (1, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]

        ans = [[0]*col for _ in range(row)]

        for r in range(row):
            for c in range(col):
                live = 0

                for i, j in direction:
                    if inbound(r+i, c+j) and board[r+i][c+j]:
                        live += 1

                if board[r][c]:

                    if live == 2 or live == 3:
                        ans[r][c] = 1
                else:
                    if live == 3:
                        ans[r][c] = 1

        for r in range(row):
            board[r] = ans[r]



        