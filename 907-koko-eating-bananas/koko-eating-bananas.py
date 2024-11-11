class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l<=r:
            k = (l+r)//2
            time = 0
            for a in piles:
                time += (a+k-1)//k
                if time>h: break
            if time<=h:
                r= k-1
            else:
                l= k+1
        return r+1



        