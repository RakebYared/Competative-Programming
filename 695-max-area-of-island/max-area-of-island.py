class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        ans = 0


        direction = [[0,1], [0,-1], [1,0], [-1,0]]

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs(cell):
            nonlocal ans

            stack = [cell]
            area = 0

            while stack:

                area += 1
                row, col = stack.pop()
                
                
                for r, c in direction:
                    nr, nc = row + r, col + c

                    if inbound(nr, nc) and grid[nr][nc]:
                        stack.append([nr,nc])
                        grid[nr][nc] = 0

            ans = max(ans, area)

        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    grid[r][c] = 0
                    dfs([r, c])

        return ans

        