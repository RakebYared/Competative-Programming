class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]
        vis = ['']*n

        ans = []

        for a, b in prerequisites:
            graph[a].append(b)


        def dfs(node):
            nonlocal ans
            
            vis[node] = 'G'
            
            for nei in graph[node]:
                
                if vis[nei] == 'G':
                    return False
                
                if not vis[nei] and not dfs(nei):
                    return False

            ans.append(node)
            vis[node] = 'B'
            return True

        for node in range(n):
            if not vis[node] and not dfs(node):
                return []
        
        return ans