class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        dp = ['']*n
        
        safe_node = []

        def dfs(node):

            if dp[node]:
                return True if dp[node] == '1' else False

            dp[node] = 'g' 

            if not len(graph[node]):
                dp[node] = '1'
                return True

            for nei in graph[node]:
                if not dfs(nei) or dp[nei] == 'g':
                    dp[node] = '0'
                    return False
            
            dp[node] ='1'
            return True

        for node in range(n):

            if dfs(node):
                safe_node.append(node)

        return safe_node

                


        