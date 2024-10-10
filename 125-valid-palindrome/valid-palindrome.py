class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alp(s) -> bool:
            if ord(s.lower())>=97 and ord(s.lower())<=122:
                return True 
            elif ord(s.lower())>=48 and ord(s.lower())<=57:
                return True
            else:
                return False
        l = 0
        r = len(s)-1
        while l<r:
            while not alp(s[l]) and l<r:
                l+=1
            while not alp(s[r]) and l<r:
                r-=1
            if l<r and s[l].lower()!= s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True
       