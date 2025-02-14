class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ans_range = int(c**(1/2))

        for a in range(ans_range + 1):
            b_squared = c - a**2
            b = b_squared**(1/2)

            if not b - int(b) :
                return True
        
        return False 




