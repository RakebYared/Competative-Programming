class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(n+1)]
        size = [1]*(n+1)

        def find(node):

            if parent[node] == node:
                return node
            parent[node] = find(parent[node])

            return parent[node]

        def union(x, y):

            x = find(x)
            y = find(y)

            if x == y:
                return True

            if size[x] > size[y]:
                parent[y] = x
                size[x] += y

            else :
                parent[x] = y
                size[y] += size[x]   


        for x,y in edges:
           
            if union(x,y):
                return [x,y]  