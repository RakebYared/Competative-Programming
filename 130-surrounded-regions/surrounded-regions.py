class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

        n, m = len(board), len(board[0])

        direction = [[0,1], [0,-1], [1,0], [-1,0]]

        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m

        def dfs(stack):
            
            while stack:
                row, col = stack.pop()

                for r,c in direction:
                    nr, nc = row + r, col + c

                    if inbound(nr, nc) and board[nr][nc] == 'O':
                        board[nr][nc] = 'I'
                        stack.append([nr, nc])
                        

        for r in range(n):
            for c in range(m):
                if r == 0 or r == n-1 or c == 0 or c == m-1:
                    if board[r][c] == 'O':
                        board[r][c] = 'I'
                        dfs([[r,c]])

        for r in range(n):
            for c in range(m):
                if board[r][c] == 'I':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'







        