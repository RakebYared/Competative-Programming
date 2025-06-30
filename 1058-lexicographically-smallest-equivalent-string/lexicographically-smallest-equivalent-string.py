class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        parent = [i for i in range(26)]
        size = [1]*26
        rep = [i for i in range(26)]


        def find(x):

            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
    
        def union(x, y):

            x = find(x)
            y = find(y)

            if x == y:
                return

            if size[y] > size[x]:
                x, y = y, x
            
            parent[y] = x
            size[x] += size[y]
            rep[x] = min(rep[x], rep[y])
    
        for x,y in zip(s1, s2):
            union(ord(x)-97, ord(y)-97)
        
        ans = []

        for letter in baseStr:
            x = find(ord(letter)-97)
            ans.append(chr(rep[x] + 97))
        
        return ''.join(ans)



        