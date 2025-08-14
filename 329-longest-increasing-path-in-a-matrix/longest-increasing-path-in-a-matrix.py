class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        n, m = len(matrix), len(matrix[0])
        direction = [[0,1], [0, -1], [1,0], [-1,0]]

        def inbound(r, c):
            return r < n and r >= 0 and c < m and c >= 0

        dp = [[0]*m for _ in range(n)]
        ans = 1

        def dfs(r, c):

            max_level = 0

            if dp[r][c]:
                return dp[r][c]

            for dr , dc in direction:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and matrix[nr][nc] > matrix[r][c]:
                    cur_level = dfs(nr, nc)
                    max_level = max(max_level, cur_level)

            dp[r][c] = max_level + 1
            return dp[r][c]

        for r in range(n):
            for c in range(m):
                ans = max(ans, dfs(r, c))
        
        return ans
                



