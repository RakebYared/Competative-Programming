class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:

        len_row, len_col = len(grid), len(grid[0])

        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        def inbound(row, col):
            return 0 <= row < len_row and 0 <= col < len_col

        vis = [[-1]*len_col for _ in range(len_row)]


        queue = deque() 

        for r in range(len_row):
            for c in range(len_col):
                if grid[r][c] == 1:
                    queue.append([r,c])
                    vis[r][c] = 0

        while queue:

            n = len(queue)

            for _ in range(n):
                row, col = queue.popleft()

                for r, c in direction:
                    new_r, new_c = row + r, col + c

                    if inbound(new_r, new_c) and vis[new_r][new_c] == -1:
                        queue.append([new_r, new_c])
                        vis[new_r][new_c] = vis[row][col] + 1
        
        return vis