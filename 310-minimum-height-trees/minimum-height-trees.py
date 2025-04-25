class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]
        edge = [0]*n

        if n == 1:
            return [0]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        q = deque()

        for node in range(n):
            edge[node] = len(graph[node]) - 1
            if not edge[node]:
                q.append(node)

        ans = []

        while q:
            ans = list(q)
            child = len(q)

            for _ in range(child):
                node = q.popleft()

                for nei in graph[node]:
                    edge[nei] -= 1
                    if not edge[nei]:
                        q.append(nei)
        
        return ans



            
        

        
        
    



