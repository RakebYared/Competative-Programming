class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            if store.get(nums[i], -1) >= 0:
                return [i, store[nums[i]]]
            store[target-nums[i]] = i
            
        