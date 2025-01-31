class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        n = [i for i in range(1,n+1)] + [i for i in range(n-1,1,-1)]
        return n[time%len(n)]

        

