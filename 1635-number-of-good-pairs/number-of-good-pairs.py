class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        s = defaultdict(int)
        for a in nums:
            s[a]+=1
            c += s[a]-1
        return c
        