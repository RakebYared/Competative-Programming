class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        len_r, len_c = len(mat), len(mat[0])

        direction = [[1,0], [0,1], [-1,0],[0,-1]]

        def inbound(r, c):
            return 0 <= r < len_r and 0 <= c < len_c

        q = deque()
        vis = [[0]*len_c for _ in range(len_r)]

        for r in range(len_r):
            for c in range(len_c):
                if not mat[r][c]:
                    q.append([r,c])
                    vis[r][c] = 1


        step = 0

        while q:
            step += 1

            n = len(q)

            for _ in range(n):
                cr, cc = q.popleft()

                for r,c in direction:
                    nr, nc = cr + r, cc + c

                    if inbound(nr, nc) and not vis[nr][nc] and mat[nr][nc]:
                        mat[nr][nc] = step
                        q.append([nr,nc])
                        vis[nr][nc] = 1

        return mat

        