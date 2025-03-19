class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        def calc(val, nums):
            if not len(nums):
                return
            
            for i in range(len(nums)):
                ans.add(tuple(val + [nums[i]]))
                calc(val + [nums[i]], nums[i+1:])
        
        calc([], nums)
                
        ans = [list(x) for x in ans]
        ans.append([])
        return ans 
        