class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for a in s:
            while i<len(t) and a!=t[i]:
                i+=1
            if i >= len(t):
                return False
            i+=1
        return True

        