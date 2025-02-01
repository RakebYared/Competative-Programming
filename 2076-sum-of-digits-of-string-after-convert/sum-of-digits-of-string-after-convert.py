class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = []

        for l in s:
            convert = str(ord(l)-ord('a')+1)
            res += [digits for digits in convert]

        for _ in range(k):
            res = list(map(int,res))
            total = str(sum(res))
            res = [a for a in total]
        return int(''.join(res))
        
        