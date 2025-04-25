class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = defaultdict(list)
        indegree = defaultdict(int)
        n = len(quiet)

        for a,b in richer:
            graph[a].append(b)
            indegree[b] += 1
            
        ans = { person : person for person in range(n)}
        
        q = deque()

        for node in range(n):
            if not indegree[node]:
                q.append(node)
        


        while q:

            node = q.popleft()

            for nei in graph[node]:

                indegree[nei] -= 1

                ans[nei] = min([ans[nei], ans[node]], key = lambda x: quiet[x])

                if not indegree[nei]:
                    q.append(nei)

        return list(ans.values())


            
        