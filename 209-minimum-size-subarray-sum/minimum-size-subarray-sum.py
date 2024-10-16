class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        counter = [0,0] # sum, length
        l = 0
        for r in range(len(nums)):
            counter[0]+=nums[r]
            while counter[0]>=target:
                counter[1] = min(counter[1], r-l+1) if min(counter[1], r-l+1)!=0 else r-l+1
                counter[0]-=nums[l]
                l+=1
        return counter[1]     
        