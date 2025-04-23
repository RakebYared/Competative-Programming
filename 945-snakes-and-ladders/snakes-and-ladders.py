class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)

        def get_cell(x):
            x -= 1
            row = x // n

            col = x % n 

            if row % 2:
                return n-row-1 , n - col - 1
            else:
                return n-row-1, col


        q = deque([[1, 0]])

        vis = [0]*(n**2 + 1)

        while q:

            c = len(q)
            for _ in range(c):
                cell, steps = q.popleft()

                if cell == n**2:
                    return steps

                for i in range(1,7):
                    if cell + i > n**2:
                        break
                    
                    r, c = get_cell(cell + i)

                    if board[r][c] == -1:
                        
                        if not vis[cell + i]:
                            q.append([cell + i, steps + 1])
                            vis[cell + i] = 1
                    
                    else:
                        if not vis[board[r][c]]:
                            q.append([ board[r][c], steps + 1])
                            vis[board[r][c]] = 1

        return -1
