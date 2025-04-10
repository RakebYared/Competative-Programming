class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:

        row_len, col_len = len(grid), len(grid[0])

        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        visited = [[0]*col_len for _ in range(row_len)]

        def inbound(row, col):
            return 0 <= row < row_len and 0 <= col < col_len
        
        def dfs(stack):
            ans = 0

            while stack:
                row, col = stack.pop()

                for r, c in direction:
                    new_row, new_col = row + r, col + c

                    if not inbound(new_row, new_col):
                        ans += 1
                    elif not grid[new_row][new_col]:
                        ans += 1

                    elif not visited[new_row][new_col]:
                        visited[new_row][new_col] = 1
                        stack.append([new_row, new_col])

            return ans
            
        
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c]:
                    visited[r][c] = 1
                    return dfs([[r, c]])

         

       