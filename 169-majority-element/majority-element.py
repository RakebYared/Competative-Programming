class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = defaultdict(int)
        for a in nums:
            store[a]+=1
            if store[a] > len(nums)//2:
                return a

        