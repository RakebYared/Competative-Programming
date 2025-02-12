class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        location = defaultdict(int)

        for i in range(len(s)):
            location[s[i]] = i
        
        ans = []
        start = 0

        while start < len(s):
            end = location[s[start]]
            i = start

            while i < end and end < len(s):
                if location[s[i]] > end:
                    end = location[s[i]]
                i += 1

            ans.append(end - start + 1)
            start = end + 1
        
        return ans
        



