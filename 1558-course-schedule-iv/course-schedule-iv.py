class Solution:
    def checkIfPrerequisite(self, n: int, edge: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = [[] for _ in range(n)]
        indegree = [0]*n
        pre = [[0]*n for _ in range(n)]

        for a,b in edge:
            graph[a].append(b)
            indegree[b] += 1

        stack = []

        for i in range(n):
            if not indegree[i]:
                stack.append(i)

        while stack:
            node = stack.pop()

            for nei in graph[node]:
                indegree[nei] -= 1
                pre[nei][node] = 1

                for i in range(n):
                    if pre[node][i]:
                        pre[nei][i] = 1
                
                if not indegree[nei]:
                    stack.append(nei)
        
        ans = []
        for u, v in queries:
            if pre[v][u]:
                ans.append(True)
            else:
                ans.append(False)

        return ans



    