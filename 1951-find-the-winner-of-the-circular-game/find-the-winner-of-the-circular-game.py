class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [num for num in range(1,n+1)]
        i = 0
        k-=1

        while len(nums) > 1:
            out = (i+k)% len(nums)
            i = out
            nums.pop(out)
        return nums[0]
            
