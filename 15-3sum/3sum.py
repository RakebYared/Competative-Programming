class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        i=0
        nums = sorted(nums)
        while i<len(nums)-2 and nums[i]<=0:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            l, r = i+1, len(nums)-1
            
            while l<r:
                sums = nums[l]+nums[r]+nums[i]
                if sums == 0:
                    ans.append([nums[l],nums[i],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif sums > 0:
                    r-=1
                else:
                    l+=1
            i+=1
        return ans 
            

    