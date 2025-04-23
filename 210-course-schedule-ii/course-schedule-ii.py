class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]
        in_degree = [0]*n
        ans = []

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        queue = deque()

        for node in range(n):
            if not in_degree[node]:
                queue.append(node)
                

        
        while queue:
            node = queue.popleft()
            ans.append(node)
            
            for nei in graph[node]:
                in_degree[nei] -= 1

                if not in_degree[nei]:
                    queue.append(nei)

        
        return ans if len(ans) == n else []


        


        


        

        