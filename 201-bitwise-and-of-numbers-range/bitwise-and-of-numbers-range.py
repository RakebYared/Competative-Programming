class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0

        
        for b in range(32):

            if right - left <= 2**b:
                
                if (right >> b) & 1 and (left >> b) & 1:
                    ans |= (1 << b)
        
        return ans
