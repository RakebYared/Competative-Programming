class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):            
            
            if nums[i] and nums[i] != i + 1:
                new_i = nums[i] - 1

                nums[new_i], nums[i] = nums[i], nums[new_i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] == 0:
                return i + 1
       
        return 0
        