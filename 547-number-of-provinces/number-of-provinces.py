class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        graph = [[] for _ in range(n)]
        vis = [0]*n

        for r in range(n):
            for c in range(n):
                if r == c:
                    continue
                if isConnected[r][c]:
                    graph[r].append(c)

        print(graph)

        def dfs(node):
            
            vis[node] = 1

            for nei in graph[node]:
                if not vis[nei]:
                    dfs(nei)
        

        ans = 0

        for node in range(n):
            if not vis[node]:
                ans += 1
                dfs(node)

        return ans

        
       