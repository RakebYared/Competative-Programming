class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row_len, col_len = len(grid), len(grid[0])

        def inbound(row, col):
            return 0 <= row < row_len and 0 <= col < col_len

        direction = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(row, col):
            grid[row][col] = 0
            print(row, col)

            for r, c in direction:
                new_row, new_col = row + r, col + c

                if inbound(new_row, new_col) and grid[new_row][new_col] == '1':
                    dfs(new_row, new_col)

        ans = 0
        
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        
        return ans