class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        visited = ['']*(n+1)

        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        
        def dfs(node, side):


            visited[node] = side

            for n in graph[node]:
                if not visited[n]:
                    if not dfs(n,'A' if side == 'B' else 'B'):
                        return False
                    
                else:
                    if visited[n] == side:
                        return False
            
            return True
            
        
        for person in range(1, n+1):

            if not visited[person]:
                if not dfs(person, 'A'):
                    return False
        
        return True