class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ps = [0]*(len(s)+1)
        for st,e,d in shifts:
            ps[st] += d or -1
            ps[e+1] -= d or -1

        res = "" 
        for i in range(len(s)):
            if i!=0: ps[i] += ps[i-1]
            res+= chr(((ord(s[i])-ord('a')+ps[i])%26)+ord('a'))
        return res
        