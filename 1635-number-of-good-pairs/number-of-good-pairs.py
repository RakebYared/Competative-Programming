class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        store = defaultdict(int)
        for a in nums:
            if store[a]!=0:
                res+= store[a]
                store[a]+=1
            else:
                store[a]=1

        return res