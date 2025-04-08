class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for i, val in enumerate(equations):
            nume, deno = val
            graph[nume].append([deno, values[i]])
            graph[deno].append([nume, 1/values[i]])
        

        def dfs(vertix, visited, weight, des):
    
            visited.add(vertix)

            
            if vertix == des:
                return weight 

            for n,w in graph[vertix]:
                if n not in visited:
                    ans = dfs(n, visited, weight * w, des)
                    if ans != -1:
                        return ans
            
            return -1

        ans = []

        for source, des in queries:
            if source not in graph or des not in graph:
                ans.append(-1)
            else:
                ans.append(dfs(source, set(), 1, des))
        
        return ans