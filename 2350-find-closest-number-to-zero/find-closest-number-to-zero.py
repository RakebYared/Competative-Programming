class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for a in nums:
            if abs(a)< abs(res):
                res = a
            elif abs(a)==abs(res):
                res = max(a, res)
        return res

                

        