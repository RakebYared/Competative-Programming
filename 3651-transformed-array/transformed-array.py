class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rev = nums[::-1]
        res = []
        for i in range(n):
            if nums[i]>0:
                res.append(nums[(i+abs(nums[i]))%n])
            elif nums[i]<0:
                res.append(rev[(n-1-i+abs(nums[i]))%n])
            else: 
                res.append(nums[i])
        return res  

        