class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1list = [0]*26
        for a in s1:
            s1list[ord(a)-97]+=1

        l = 0
        while l < len(s2):
            r = l
            copylist = s1list.copy()
            while r<len(s2) and copylist[ord(s2[r])-97]-1>=0:
                copylist[ord(s2[r])-97]-=1
                r+=1
            if r-l == len(s1):
                return True
            if r==len(s2): break
            while l<r and s2[l]!=s2[r]:
                l+=1
            l+=1
        return False

