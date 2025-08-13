class union_find:
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
    def numSimilarGroups(self, strs: List[str]) -> int:



        n = len(strs)

        uf = union_find(n)

        def similar(str1, str2):
            flag = 0
            wrong = 0


            for i in range(len(str1)):

                if str1[i] != str2[i]:

                    if not flag:
                        wrong = i
                        flag = 1

                    elif flag == 1:

                        if str2[i] == str1[wrong] and str2[wrong] == str1[i]:
                            flag = 2
                        else:
                            return False
                    
                    else:
                        return False

               
            return True

        for i in range(n):
            for j in range(i+1, n):

                if similar(strs[i], strs[j]):
                    uf.union(i, j)
                    print('h')

        ans = set()
        
        for i in range(n):
            ans.add(uf.find(i))
        
        return len(ans)
        