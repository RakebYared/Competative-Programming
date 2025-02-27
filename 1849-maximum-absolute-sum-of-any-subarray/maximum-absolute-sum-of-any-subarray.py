class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        max_ = 0
        min_ = 0

        ps = 0 
        ans = 0

        for num in nums:
            ps += num

            if ps < 0:
                min_ = min(min_, ps)
                ans = max(ans, abs(ps - max_))
            else:
                max_ = max(max_, ps)
                ans = max(ans, abs(ps - min_))
        
        return ans



        