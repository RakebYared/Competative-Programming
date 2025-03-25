class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        
        a = [num for num in range(len(nums), 0, -1)]
        stack = []

        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                a[stack[-1]] = i - stack[-1] 
                stack.pop()
            
            stack.append(i)


        b = [num for num in range(1, len(nums)+1)]
        stack = []

        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                b[stack[-1]] = stack[-1] - i 
                stack.pop()
            
            stack.append(i)

        ans = 0
        
        for i in range(len(nums)):
            ans += (b[i] * a[i] * nums[i])
        
        return ans % (10**9 + 7)

      

        