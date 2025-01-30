class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alp(s) -> bool:
            if ord(s.lower())>=97 and ord(s.lower())<=122:
                return True 
            elif ord(s.lower())>=48 and ord(s.lower())<=57:
                return True
            else:
                return False
        
        
        s = list(val for val in s if alp(val))
        l, r = 0, len(s)-1
        while l<r:
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True