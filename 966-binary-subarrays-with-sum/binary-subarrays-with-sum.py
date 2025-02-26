class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        running_sum = 0 
        store = defaultdict(int)
        store[0] = 1
        count = 0

        for num in nums:
            running_sum += num
            count += store[running_sum - goal]
            store[running_sum] += 1
        
        return count
        