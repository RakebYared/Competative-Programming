class Solution:
    def dividePlayers(self, nums: List[int]) -> int:
        nums.sort()
        chem = 0 
        teamSum = nums[0] + nums[-1]
        for i in range(len(nums)//2):
            if nums[i] + nums[len(nums)-1-i] != teamSum:
                return -1
            chem += (nums[i]*nums[len(nums)-1-i])
        return chem

        