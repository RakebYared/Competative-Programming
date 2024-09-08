class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        store = defaultdict(int)
        for a in nums:
            store[a]+=1
        for n in store.values():
            count+= ((n-1)*n)//2
        return count 
        