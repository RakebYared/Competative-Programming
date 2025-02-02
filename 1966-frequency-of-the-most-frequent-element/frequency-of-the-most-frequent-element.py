class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int: 
        '''
        its better to start working on numbers that are close to each other
        so between consqueative number how long can i extend my window without the difference exceeding k
        reference point should be the max number
        as we increase the winow the new element will be compared to the previous one 
        so maybe o(n)
        adding :
            dif += (nums[r]-nums[r-1])*(length of the old window before adding nums[r])
        removing :
        differ -= nums[r]-nums[l]

        '''
        if len(nums) == 1:
            return 1

        nums.sort()
        max_frequency = 0
        difference = 0
        l = 0

        for r in range(1,len(nums)):
            difference += (nums[r]-nums[r-1])*(r-l)

            while difference>k and l<=r:
                difference -= nums[r]-nums[l]
                l+=1
            
            max_frequency = max(max_frequency, r-l+1)
        
        return max_frequency 



