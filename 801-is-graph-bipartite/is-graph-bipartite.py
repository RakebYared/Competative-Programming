class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        visited = ['']*n

        def dfs(node, side):

            visited[node] = side

            for n in graph[node]:
                if not visited[n]:
                    ans = dfs(n, 'A' if side == 'B' else 'B')
                    if not ans:
                        return False

                else:
                    if side == visited[n]:
                        return False

            return True



        for node in range(n):
            if not visited[node]:
                if not dfs(node, 'A'):
                    return False

        return True
        
    