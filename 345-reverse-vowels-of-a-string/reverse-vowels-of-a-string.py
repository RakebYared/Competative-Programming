class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowel = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}
        r = len(s) - 1
        l = 0
        s = list(s)

        while l < r:
            if s[l] in vowel:
                while s[r] not in vowel:
                    r -= 1
                s[r], s[l] = s[l], s[r]   
                r -= 1 
            l += 1     
        
        return ''.join(s)
            




        