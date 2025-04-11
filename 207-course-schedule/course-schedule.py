class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        visited = ['']*numCourses


        for a, b in prerequisites:
            graph[a].append(b)

       

        def dfs(node):
            visited[node] = '1'

            for neigh in graph[node]:
                if not visited[neigh]:
                    ans = dfs(neigh)

                    if not ans:
                        return False
                
                else:
                    if visited[neigh] == '1':
                        return False
                   
            
            visited[node] = '0'
            return True

        
        for node in range(numCourses):
            
            if not visited[node]:
                ans = dfs(node)
                if not ans:
                    return False
        
        return True


        