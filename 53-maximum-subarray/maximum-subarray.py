class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_ = -float('inf')
        min_ = 0

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        for num in nums:
            max_ = max(max_, num - min_)
            min_ = min(min_, num)
        
        return max_
            
        