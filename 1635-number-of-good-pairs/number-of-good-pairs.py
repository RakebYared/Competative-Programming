class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        store = defaultdict(int)
        for a in nums:
            store[a]+=1
            c += store[a]-1
        return c
        