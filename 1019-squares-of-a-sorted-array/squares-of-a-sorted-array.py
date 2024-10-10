class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]: 
        l, r= 0, len(nums)-1
        ans = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[l]) > abs(nums[r]):
                ans[i] = pow(nums[l],2)
                l+=1
            else: 
                ans[i] = pow(nums[r],2)
                r-=1

        return ans
        