class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        store = defaultdict(int)
        for a in nums:
            store[a]+=1
        for n in store.values():
            c+= ((n-1)*n)//2
        return c
        