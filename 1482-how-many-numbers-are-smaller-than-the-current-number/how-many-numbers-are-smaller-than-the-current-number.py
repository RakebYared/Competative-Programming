class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = [0]*(max(nums)+1)

        for num in nums:
            counter[num] += 1
        
        for i in range(1,len(counter)):
            counter[i] += counter[i-1]

        ans = [0]*len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                ans[i] = counter[nums[i]-1]
        
        return ans


        
        




