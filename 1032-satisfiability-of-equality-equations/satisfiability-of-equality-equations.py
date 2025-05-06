class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        equations.sort(key = lambda x : x[1], reverse = True)
        
        parent = [i for i in range(26)]
        size = [1]*26

        def find(x):
            while x != parent[x]:
                x = parent[x]
            
            return x

        def union(x, y):
            x = find(x)
            y = find(y)

            if x == y:
                return 

            if size[x] > size[y]:
                parent[y] = x
                size[x] += size[y]
            else:
                parent[x] = y
                size[y] += size[x]


        for eq in equations:

            a, b, sign = ord(eq[0]) - 97 , ord(eq[3]) - 97 , eq[1]

            if sign == '=':
                union(a, b)
            else:
                if find(a) == find(b):
                    return False

        return True
        