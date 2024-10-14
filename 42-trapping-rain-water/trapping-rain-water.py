class Solution:
    def trap(self, h: List[int]) -> int:
        l,r = 0, len(h)-1
        ans = 0 
        while l<r:
            con = min(h[r], h[l])
            while h[l]<=con and l<r:
                ans += con - h[l]
                l+=1
            while h[r]<=con and l<r:
                ans += con-h[r]
                r-=1
        return ans

            
        