class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")
        res = []
        for word in words:
            n = len(word)
            if n == len([l for l in word if l in row1]) or n == len([l for l in word if l in row2]) or n == len([l for l in word if l in row3]):
                res.append(word)
        return res

        