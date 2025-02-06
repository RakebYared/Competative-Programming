class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [num for num in range(1,n+1)]
        i = 0

        while len(nums) > 1:
            out = (i+k-1)% len(nums)
            i = out
            nums.pop(out)
        return nums[0]
            
