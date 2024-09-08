class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[i]==nums[j]:
                    res+=1
                j+=1
            i+=1
        return res