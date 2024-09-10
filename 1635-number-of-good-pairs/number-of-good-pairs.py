class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        sto = defaultdict(int)
        for a in nums:
            sto[a]+=1
            c += sto[a]-1
        return c
        