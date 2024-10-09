class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = [0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            store[ord('a')-ord(s[i])]+=1
            store[ord('a')-ord(t[i])]-=1
        return store == [0]*26

               
           