class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:


        n = len(grid)

        ngrid = [[0]*(3*n) for _ in range(n*3)]

        for r in range(n):
            for c in range(n):

                if grid[r][c] == '\\':

                    nr, nc = r*3, c*3
                    for _ in range(3):
                        ngrid[nr][nc] = 1
                        nr += 1
                        nc += 1

                elif grid[r][c] == '/':
                    nr, nc = r*3, c*3 + 2

                    for _ in range(3):
                        ngrid[nr][nc] = 1
                        nr += 1
                        nc -= 1
        
        
        n *= 3 

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n
        
        direction = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(row, col):
            stack = [[row, col]]
            ngrid[row][col] = 1

            while stack:

                row, col = stack.pop()

                for r, c in direction:
                    nr, nc = row + r, col + c

                    if inbound(nr,nc) and not ngrid[nr][nc]:
                        ngrid[nr][nc] = 1
                        stack.append([nr, nc])

        ans = 0
        for r in range(n):
            for c in range(n):
                if not ngrid[r][c]:
                    ans += 1     
                    dfs(r,c)
                    

        return ans

                




        