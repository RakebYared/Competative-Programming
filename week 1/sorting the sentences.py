class Solution:
    def sortSentence(self, sen: str) -> str:
        s = sen.split()
        res = [""]*len(s)
        for i in range(len(s)):
            digit = int(s[i][-1])
            res[digit-1] = s[i][0:-1]
        return ' '.join(res)
            