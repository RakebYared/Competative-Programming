class Solution:
    def judgeSquareSum(self, c: int) -> bool:
# 0 1 3.......-2 -1 sqrt(c) o(n): 

        l, r = 0, int(sqrt(c))
        while l<=r:
            res = l*l + (r*r)
            if res>c:
                r-=1
            elif res<c:
                l+=1
            else:
                return True
        return False