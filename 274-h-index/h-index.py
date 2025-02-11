class Solution:
    def hIndex(self, citations: List[int]) -> int:

        ans = 0
        citations.sort()
        i = 0
        n = len(citations)

        while i < n-ans:
            ans = max(min(n-i, citations[i]), ans)
            i+=1
        
        return ans

        