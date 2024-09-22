class Solution:
    def titleToNumber(self, col: str) -> int:
        res=0
        i = len(col)-1
        for a in col:
            res+=pow(26,i)*(ord(a)-64)
            i-=1
        return res