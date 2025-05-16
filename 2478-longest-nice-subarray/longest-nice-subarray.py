class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        checker = 0

        l = 0
        ans = 0

        for r in range(len(nums)):
            
            while nums[r] & checker:
                checker ^= nums[l]
                l += 1
                

            checker |= nums[r]
            ans = max(ans , r - l + 1)

        return ans


        