class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:

        row_length, col_length = len(grid), len(grid[0])
        visited = [[0]*col_length for _ in range(row_length)]

        direction = [(0,1), (1,0), (0,-1), (-1,0)]

        def inbound(r, c):            
            return 0 <= r < row_length and 0 <= c < col_length
        
        ans = 0
        
        def dfs(row, col):
            nonlocal ans

            visited[row][col] = 1

            for r, c in direction:
                new_row, new_col = row + r, col + c

                if not inbound(new_row, new_col):
                    ans += 1
                
                elif not visited[new_row][new_col]: 
                    if grid[new_row][new_col]:
                        dfs(new_row, new_col)
                    else:
                        ans += 1
        
        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j]:
                    dfs(i,j)
                    return ans

