class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        pair_counter = 0
        left_over = 0

        for num in counter:
            if counter[num]%2:
                left_over += 1
                pair_counter += ((counter[num]-1)//2) 
            else:
                pair_counter += (counter[num]//2)
        
        
        return [pair_counter, left_over]
        