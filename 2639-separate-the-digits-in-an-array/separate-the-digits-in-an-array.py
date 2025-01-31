class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums = list(map(str, nums))
        nums = ''.join(nums)
        return [int(a) for a in nums]
        