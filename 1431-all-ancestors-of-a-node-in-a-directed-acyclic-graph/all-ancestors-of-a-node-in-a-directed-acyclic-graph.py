class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = [[] for _ in range(n)]

        indegree = [0]*n
        ans = [set() for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            indegree[b] += 1

        q = deque()

        for i in range(n):
            if not indegree[i]:
                q.append(i)

        while q:

            node = q.popleft()
            for child in graph[node]:
                indegree[child] -= 1

                ans[child].add(node)
                ans[child].update(ans[node])

                if not indegree[child]:
                    q.append(child)

        ans = [sorted(val) for val in ans]
        return ans
        