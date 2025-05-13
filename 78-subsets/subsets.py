class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        

        for num in range(2 ** len(nums)):
            num = bin(num)[2:]

            num = '0'*(len(nums) - len(num)) + num
            val = []


            for i in range(len(num)):
                if num[i] == '1':
                    val.append(nums[i])
            
            ans.append(val)
        
        return ans
        

        


            
                

