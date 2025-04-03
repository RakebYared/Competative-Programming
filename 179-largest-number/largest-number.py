class Solution:
    def largestNumber(self, nums: List[int]) -> str:
    
        nums = [str(num) for num in nums]
        nums.sort(key = lambda x: x*(11-len(x)), reverse = True)
        nums = ''.join(nums)
        if nums == '0'*len(nums):
            return '0'
        return nums


