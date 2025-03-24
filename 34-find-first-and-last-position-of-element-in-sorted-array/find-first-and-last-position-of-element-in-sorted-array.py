class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = bisect_left(nums, target), bisect_right(nums, target)

        if start == end:
            return [-1,-1]
        
        return [start, end - 1]