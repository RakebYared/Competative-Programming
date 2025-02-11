class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """s = list(map(str, nums))
        max_place = len(max(s, key=len))

        s = sorted(s, key = lambda x: x + x[-1]*(max_place-len(x)), reverse = True)
        return ''.join(s)
        """

        nums = list(map(str, nums))

        # bubble sort
        for i in range(len(nums)):
            for j in range(1, len(nums)-i):
                if nums[j-1] + nums[j] < nums[j] + nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
        
        if nums == ['0']*len(nums):
            return "0"
            
        return ''.join(nums)


