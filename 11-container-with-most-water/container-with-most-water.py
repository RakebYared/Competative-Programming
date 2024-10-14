class Solution:
    def maxArea(self, h: List[int]) -> int:
        ans, l, r= 0, 0, len(h)-1
        while l<r:
            if h[l]<h[r]:
                ans = max(ans, h[l]*(r-l))
                l+=1
            elif h[l]>h[r]:
                ans = max(ans, h[r]*(r-l))
                r-=1
            else:
                ans = max(ans, h[r]*(r-l))
                r-=1
                l+=1
        return ans
