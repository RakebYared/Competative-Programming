class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, two = 0, len(nums)-1
        i = 0

        while i < len(nums):
            if i > two:
                break
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
                zero += 1
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            else:
                i += 1

            