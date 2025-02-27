class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones = 0
        zeros = 0
        store = {0:-1}  # zeros - one : index 
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                zeros += 1
            
            if (zeros - ones) in store:
                ans = max(ans, i - store[zeros - ones])
            else:
                store[zeros - ones] = i
        
        return ans

            


       
