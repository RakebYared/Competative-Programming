class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        minimum = abs(min(nums))
        counter = [0] * (max(nums) + minimum + 1)

        for num in nums:
            counter[num + minimum] += 1
        
        ans = []
        for i in range(len(counter)):
            ans += [i-minimum]*counter[i]

        return ans        
        
        