class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [num for num in range(1,n+1)]
        i = 0
        k-=1

        while len(nums) > 1:
            out = (i+k)% len(nums)
            if out == 0:
                nums = nums[1:]
                i = 0
            elif out == len(nums)-1:
                nums = nums[:len(nums)-1]
                i = 0
            else:
                nums = nums[:out] + nums[out+1:]
                i = out
        return nums[0]
            
