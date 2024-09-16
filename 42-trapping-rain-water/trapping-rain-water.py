class Solution:
    def trap(self, h: List[int]) -> int:
        l, r, add= 0, len(h)-1, 0
        while l<r:
            con = min(h[l],h[r])
            while l<r:
                if h[l]<=h[r]:
                    l+=1
                    if h[l]<con: add+= (con-h[l])  
                    else: break
                else:
                    r-=1
                    if h[r]<con: add+= (con-h[r])  
                    else: break
        return add

        