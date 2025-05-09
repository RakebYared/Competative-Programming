class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        store = defaultdict(list)

        for left, right in edges:
            store[left].append(right)
            store[right].append(left)

        def dfs(node, visited):

            visited.add(node)
            for n in store[node]:
    
                if n == destination:
                    return True

                if n not in visited and dfs(n, visited):
                    return True

            return False
        
        if source == destination:
            return True

        return dfs(source, set())