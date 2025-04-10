class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zeros = 0
        max_ = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            max_ = max(max_, r-l+1)
        
        return max_



        