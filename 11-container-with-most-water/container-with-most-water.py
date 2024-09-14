class Solution:
    def maxArea(self, h: List[int]) -> int:
        area, l, r = 0, 0, len(h)-1
        while l<r:
            if h[l]<h[r]:
                area = max(area,h[l]*(r-l))
                l+=1
            elif h[r]<h[l]:
                area = max(area,h[r]*(r-l))
                r-=1
            else:
                area = max(area,h[r]*(r-l))
                r-=1
                l+=1
        return area
                
        