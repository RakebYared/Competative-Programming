class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        interval = defaultdict(list)
        for i in range(len(s)):
            if interval[s[i]]:
                interval[s[i]][1] = i
            else:
                interval[s[i]] = [i,i]
        interval = list(interval.values())
        res = []
        i = 0
        while i<len(interval):
            start = interval[i][0]
            end = interval[i][1]
            while i<len(interval) and interval[i][0] <= end:
                end = max(end, interval[i][1])
                i+=1
            res.append(end-start+1)

        return res