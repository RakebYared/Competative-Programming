class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_jump = 0
        n = len((nums))

        for i,num in enumerate(nums):
            if i + num == n - 1:
                return True
            elif num == 0 and max_jump <= i:
                return False
            
            max_jump = max(max_jump, i + num)
                 
        return True 
        