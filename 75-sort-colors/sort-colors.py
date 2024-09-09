class Solution:
    def sortColors(self, nums: list[int]) -> None:
        l, i, r = 0, 0, len(nums) - 1
        
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif i==r:
                break
            else:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
