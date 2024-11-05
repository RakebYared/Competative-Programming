class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        while i<len(s):
            j = i+1
            while j<len(s) and  s[j]==s[j-1]:
                j+=1
            if j-i>2:
                s = s[:i+2] + s[j:]
                i+=1
            i+=1
        return s


        
            
        