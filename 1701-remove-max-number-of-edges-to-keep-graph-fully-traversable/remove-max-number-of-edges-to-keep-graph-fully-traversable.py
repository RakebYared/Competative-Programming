class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        edges.sort(reverse = True)

        alice = [i for i in range(n+1)]
        alice_size = [1]*(n+1)

        bob = [i for i in range(n+1)]
        bob_size = [1]*(n+1)

        def find(x, person):

            if person:

                while x != alice[x]:
                    alice[x] = alice[alice[x]]
                    x = alice[x]
                
            
            else:
                while x != bob[x]:
                    bob[x] = bob[bob[x]]
                    x = bob[x]
                
            return x


        def union(x,y, person) :

            if person:

                x = find(x, person)
                y = find(y, person)

                if x == y:
                    return False
                
                if alice_size[y] > alice_size[x]:
                    x, y = y, x
                
                alice[y] = x
                alice_size[x] += alice_size[y] 
                
                
            
            else:
                x = find(x, person)
                y = find(y, person)

                if x == y:
                    return False
                
                if bob_size[y] > bob_size[x]:
                    x, y = y, x
                
                bob[y] = x
                bob_size[x] += bob_size[y] 
                
            return True

        count = 0

        for t,x,y in edges:

            if t == 3:

                if union(x, y, True):
                    union(x, y, False)
                    count += 1

            elif t == 2:
                if union(x, y, False):
                    count += 1
            
            else:
                if union(x, y, True):
                    count += 1

        count = len(edges) - count
        
        return count if max(alice_size) == n and max(bob_size) == n else -1




        