class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispalindrom(s):
            for i in range(len(s)//2):
                if s[i] != s[len(s)-i-1]:
                    return False
            return True
        k = len(s)
        while k>1:
            for i in range(len(s)-k+1):
                if ispalindrom(s[i:i+k]):
                    return s[i:i+k]
            k-=1
        return(s[0])