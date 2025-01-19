class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispalindrom(s):
            for i in range(len(s)//2):
                if s[i] != s[len(s)-i-1]:
                    return False
            return True
        res = s[0]
        for i in range(len(s)-1):
            j = len(s)-1
            while j>i and j-i+1>len(res):
                if ispalindrom(s[i:j+1]):
                    res = s[i:j+1]
                    break
                j-=1
           
        return res