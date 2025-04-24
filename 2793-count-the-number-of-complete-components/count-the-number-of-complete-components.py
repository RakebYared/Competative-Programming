class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

     
        vis = [0]*n
        ans = 0

        def dfs(node):
            stack = [node]
            vis[node] = 1
            v, e = 0, 0 

            while stack:
                node = stack.pop()
                e += len(graph[node]) 
                v += 1

                for nei in graph[node]:
                    if not vis[nei]:
                        stack.append(nei)
                        vis[nei] = 1
            
            return e == ((v - 1) * v)
            


        for node in range(n):
            if not vis[node] and dfs(node):
                ans += 1

        return ans


        