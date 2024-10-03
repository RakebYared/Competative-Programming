class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        interval = sorted(interval)
        res = []
        i = 0
        while i<len(interval):
            a = interval[i][0]
            b = interval[i][1]
            while i<len(interval)-1 and b>=interval[i+1][0]:
                i+=1
                b = max(b, interval[i][1])
            res.append([a,b])
            i+=1
        return res
