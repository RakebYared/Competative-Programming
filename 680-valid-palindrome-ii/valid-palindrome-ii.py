class Solution:
    def validPalindrome(self, s: str) -> bool:        
        def isPalindrome(l,r):
            while l<r:
                if s[r] != s[l]:
                    return False
                l += 1
                r -= 1
            return True            

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if isPalindrome(l, r-1) or isPalindrome(l+1, r):
                    return True 
                else:
                    return False
                
            r -= 1
            l += 1
        return True
        