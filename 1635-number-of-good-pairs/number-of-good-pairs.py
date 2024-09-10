class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        st = defaultdict(int)
        for a in nums:
            st[a]+=1
            c += st[a]-1
        return c
        