class Solution:
    def updateBoard(self, grid: List[List[str]], click: List[int]) -> List[List[str]]:

        len_r, len_c = len(grid), len(grid[0])

        direction = [[1,0], [1,-1], [1,1], [-1,0], [-1,-1], [-1, 1], [0,1], [0,-1]]

        def count_mines(sr, sc):
            count = 0

            for r, c in direction:
                nr, nc = sr + r, sc + c

                if inbound(nr,nc) and grid[nr][nc] == 'M':
                    count += 1

            return count 

        def inbound(r, c):
            return 0 <= r < len_r and 0 <= c < len_c


        r, c = click
        vis = [[0]*len_c for _ in range(len_r)]
        vis[r][c] = 1

        stack = [[r,c]]

       
        if grid[r][c] == 'M':
            grid[r][c] = 'X'
            return grid

        while stack:

            row, col = stack.pop()
 
            if grid[row][col] == 'E':
                mine = count_mines(row, col)

                if mine:
                    grid[row][col] = str(mine)
                else:

                    grid[row][col] = 'B'
                    for r, c in direction:
                        nr, nc = row + r, col + c

                        if inbound(nr,nc) and not vis[nr][nc]:
                            stack.append([nr, nc])
                            vis[nr][nc] = 1
                        
        return grid                


