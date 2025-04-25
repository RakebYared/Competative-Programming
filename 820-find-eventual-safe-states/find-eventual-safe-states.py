class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        temp = [[] for _ in range(n)]
        indegree = [0]*n

        for node in range(n):

            for child in graph[node]:
                temp[child].append(node)
            
            indegree[node] = len(graph[node])

        graph = temp
        
        q = deque()

        for node in range(n):
            if not indegree[node]:
                q.append(node)


        ans = []

        while q:

            node = q.pop()
            ans.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1

                if not indegree[nei]:
                    q.append(nei)

        return sorted(ans)

       