class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal algo

        n = len(points)
        graph = [] # [weigth, x, y]

        for i in range(n):
            for j in range(i+1, n):

                x, y = points[i]
                xi, yi = points[j]

                dis = abs(x - xi) + abs(y - yi)

                graph.append([dis, i, j])
        
        graph.sort()

        parent = [i for i in range(n)]
        size = [1]*n

        def find(x):

            while x != parent[x]:

                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x

        def union(x, y):
            x = find(x)
            y = find(y)

            if x == y:
                return True

            if size[x] < size[y]:
                x, y = y, x

            parent[y] = x
            size[x] += size[y]
            
        ans = 0

        for dis, x, y in graph:

            if not union(x,y):
                ans += dis 
        
        return ans




