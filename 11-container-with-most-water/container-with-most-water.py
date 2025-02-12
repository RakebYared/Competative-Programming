class Solution:
    def maxArea(self, h: List[int]) -> int:

        l, r = 0, len(h) - 1
        ans = 0

        while l < r:
            if h[l] < h[r]:
                ans = max(ans, h[l]*(r - l))
                i = l + 1
                while i < r and h[l] >= h[i]:
                    i += 1
                l = i

            elif h[r] < h[l]:
                ans = max(ans, h[r]*(r - l)) 

                i = r - 1
                while i > r and h[r] >= h[i]:
                    i -= 1
                r = i

            else:
                ans = max(ans, h[r]*(r - l)) 

                i, j = l + 1, r - 1
                while i < j and h[l] >= h[i] and h[r] >= h[j]:
                    i += 1
                    j -= 1
                
                r = j
                l = i
        
        return ans
        