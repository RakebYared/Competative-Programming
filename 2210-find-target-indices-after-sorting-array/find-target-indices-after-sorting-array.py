class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            minindex = i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[minindex]:
                    minindex = j
                    
            if minindex!=i:
                nums[i], nums[minindex] = nums[minindex], nums[i]
            if nums[i] == target:
                res.append(i)
        return res



        
        