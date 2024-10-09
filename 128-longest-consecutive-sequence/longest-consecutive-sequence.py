class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0 
        ans = 0
        nums = sorted(nums)
        while i<len(nums):
            count = 0
            j = nums[i]
            while i < len(nums):
                if j == nums[i]:
                    count+=1
                    i+=1
                    j+=1
                elif j == nums[i]+1:
                    i+=1
                else:
                    break
            ans = max(ans, count)
        return ans        