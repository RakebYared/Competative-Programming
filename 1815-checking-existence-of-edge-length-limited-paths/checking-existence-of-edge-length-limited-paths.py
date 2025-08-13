'''
connect all the edges < limit and then check if they are union.
'''

class Union_Find:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.size = [1]*n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.size[y] > self.size[x]:
            x, y = y, x
        
        self.parent[y] = x
        self.size[x] += self.size[y]

        

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        union_find = Union_Find(n)

        edgeList = sorted([[w, x, y] for x,y,w in edgeList])
        queries = sorted([[l,x,y,i] for i, [x,y,l] in enumerate(queries)])

        
        pointer = 0

        ans = [None]*len(queries)

        for l,x,y,i in queries:

            while pointer < len(edgeList) and edgeList[pointer][0] < l:
                _, u, v = edgeList[pointer]
                union_find.union(u,v)
                pointer += 1
            
            ans[i] = union_find.find(x) == union_find.find(y)
        
        return ans
            

        

        
