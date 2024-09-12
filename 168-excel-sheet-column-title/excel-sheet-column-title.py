class Solution:
    def convertToTitle(self, col: int) -> str:
        res = ""
        while col > 0:
            col -= 1  
            res = chr(65 + (col % 26)) + res
            col //= 26
        return res
