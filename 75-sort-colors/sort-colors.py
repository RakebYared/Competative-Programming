class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            smallest = i
            for j in range(i+1, len(nums)):
                if nums[j]<nums[smallest]:
                    smallest = j
            nums[smallest], nums[i] = nums[i], nums[smallest]
        return nums
        