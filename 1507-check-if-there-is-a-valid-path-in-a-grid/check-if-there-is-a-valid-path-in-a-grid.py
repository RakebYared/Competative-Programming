class Solution:

    def hasValidPath(self, grid: List[List[int]]) -> bool:

        n, m = len(grid), len(grid[0])

        direction = { 'u':[-1,0], 'd':[1,0], 'l':[0,-1], 'r':[0,1]}

        point = {1:'lr', 2:'ud', 3:'ld', 4:'dr', 5:'lu', 6:'ru'}
        expect = {'u':'d', 'd':'u', 'l':'r', 'r':'l'}

        vis = [[0]*m for _ in range(n)]
        vis[0][0] = 1

        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m

        stack = [[0,0]]


        while stack:

            row, col = stack.pop()

            if [row, col] == [n-1, m-1]:
                return True

            p = grid[row][col]

            for d in point[p]:
               
                r, c = direction[d]
                nr, nc = row + r, col + c

                if inbound(nr, nc) and not vis[nr][nc] and expect[d] in point[grid[nr][nc]]:

                    vis[nr][nc] = 1
                    stack.append([nr, nc])

        return False


        


        