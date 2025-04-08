class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trust_list = [[] for _ in range(n+1)]
        trusted = [[] for _ in range(n+1)]

        for a,b in trust:
            trust_list[a].append(b)

            trusted[b].append(a)
        
        for i in range(1,n+1):
            if len(trusted[i]) == n-1 and not trust_list[i]:
                return i
        
        return -1

        


        
        