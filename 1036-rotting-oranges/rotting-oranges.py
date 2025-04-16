class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        len_row, len_col = len(grid), len(grid[0])

        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        def inbound(row, col):
            return 0 <= row < len_row and 0 <= col < len_col

        q = deque()
        oranges = 0
        count = 0

        for r in range(len_row):
            for c in range(len_col):

                if grid[r][c] == 2:
                    q.append([r,c])
                    grid[r][c] = 0
                
                if grid[r][c] == 1:
                    oranges += 1

        if not oranges:
            return 0

        while q:

            n = len(q)

            for _ in range(n):
                row, col = q.popleft()

                for r, c in direction:
                    new_r, new_c = row + r, col + c

                    if inbound(new_r, new_c) and grid[new_r][new_c]:
                        q.append([new_r, new_c])
                        oranges -= 1                          
                        grid[new_r][new_c] = 0

            count += 1

            if oranges <= 0:
                return count
        return -1