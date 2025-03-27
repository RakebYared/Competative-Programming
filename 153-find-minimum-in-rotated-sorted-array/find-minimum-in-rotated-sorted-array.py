class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while r - l > 1:
            mid = (r + l) // 2

            if nums[l] < nums[mid] and nums[r] > nums[mid]:
                r = mid
            elif nums[l] > nums[mid] and nums[r] < nums[mid]:
                l = mid
            elif nums[l] > nums[mid]:
                r = mid
            else:
                l = mid
            
        return min(nums[l], nums[r])

        