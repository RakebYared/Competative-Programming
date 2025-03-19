class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        def create(val, nums):
            if not nums:
                return 

            for i in range(len(nums)):
                ans.append(val + [nums[i]])
                create(val + [nums[i]], nums[i+1:])
            
        create([],nums)
        return sorted(ans)
                


            
        
        