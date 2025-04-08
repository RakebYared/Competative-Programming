class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for i, val in enumerate(equations):
            nume, deno = val
            graph[nume].append([deno, values[i]])
            graph[deno].append([nume, 1/values[i]])
        visited = set()
        des = -1

        def dfs(vertix):
            visited.add(vertix)
            if vertix == des:
                return 1 
            for n, w in graph[vertix]:
                if n not in visited:
                    ans = dfs(n)
                    if ans != -1:
                        return ans*w
            return -1

        ans = []

        for source, de in queries:
            if source not in graph or de not in graph:
                ans.append(-1)
            else:
                visited = set()
                des = de
                ans.append(dfs(source))
        
        return ans