class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i<len(nums):
            a = b = nums[i]
            while i<len(nums) and nums[i]==b:
                i+=1
                b+=1
            res.append(str(a)+"->"+str(b-1) if a!=b-1 else str(a))
        return res

       