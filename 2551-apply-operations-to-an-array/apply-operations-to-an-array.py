class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums[i]*= 2
                nums[i+1] = 0
                i += 1
            i+=1
        nums.sort(key = lambda x: 0 if x else 1)
        return nums
                    

        